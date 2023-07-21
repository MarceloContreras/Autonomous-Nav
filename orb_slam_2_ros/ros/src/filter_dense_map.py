#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import PointCloud2
from pcl_helpers import *
from tf_helpers import *

class RGBD_handler(object):
    def __init__(self):
        self.sub = rospy.Subscriber('/camera/depth/points',PointCloud2,self.callback,queue_size=50)
        self.pub = rospy.Publisher('/filtered_dense',PointCloud2,queue_size=50)
        self.VOXEL_SIZE = 0.05
        self.SCALE_FACTOR = 0.01

    def callback(self,msg):
        plc_cloud = ros_to_pcl(msg)
        pcl_downsampled   = self.filter_downsampling(plc_cloud)
        pcl_filtered      = self.filter_passthrough(pcl_downsampled)
        ros_filteredcloud = self.pcl_to_ros(XYZ_to_XYZRGB(pcl_filtered,[255,255,255]))
        self.pub.publish(ros_filteredcloud)
    
    def filter_downsampling(self,point_cloud):
        fvox = point_cloud.make_voxel_grid_filter()
        fvox.set_leaf_size(self.VOXEL_SIZE, self.VOXEL_SIZE, self.VOXEL_SIZE)
        pcl_downsampled = fvox.filter()
        return pcl_downsampled
    
    def filter_kmeans(self,point_cloud):
        outlier_filter = point_cloud.make_statistical_outlier_filter()
        outlier_filter.set_mean_k(15)
        outlier_filter.set_std_dev_mul_thresh(self.SCALE_FACTOR)
        cloud_filtered = outlier_filter.filter()
        return cloud_filtered

    def filter_passthrough(self,point_cloud):
        passthrough = point_cloud.make_passthrough_filter()
        filter_axis = 'y'
        min_val = -10
        max_val = 0
        passthrough.set_filter_field_name(filter_axis)
        passthrough.set_filter_limits(min_val, max_val)
        cloud_filtered = passthrough.filter()
        return cloud_filtered
    
    def pcl_to_ros(self,pcl_array):

        ros_msg = PointCloud2()
        ros_msg.header.stamp = rospy.Time.now()
        ros_msg.header.frame_id = "camera_rgb_optical_frame"
        ros_msg.height = 1
        ros_msg.width = pcl_array.size

        ros_msg.fields.append(PointField(
                                name="x",
                                offset=0,
                                datatype=PointField.FLOAT32, count=1))
        ros_msg.fields.append(PointField(
                                name="y",
                                offset=4,
                                datatype=PointField.FLOAT32, count=1))
        ros_msg.fields.append(PointField(
                                name="z",
                                offset=8,
                                datatype=PointField.FLOAT32, count=1))
        ros_msg.fields.append(PointField(
                                name="rgb",
                                offset=16,
                                datatype=PointField.FLOAT32, count=1))

        ros_msg.is_bigendian = False
        ros_msg.point_step = 32
        ros_msg.row_step = ros_msg.point_step * ros_msg.width * ros_msg.height
        ros_msg.is_dense = False
        buffer = []

        for data in pcl_array:
            s = struct.pack('>f', data[3])
            i = struct.unpack('>l', s)[0]
            pack = ctypes.c_uint32(i).value
            r = (pack & 0x00FF0000) >> 16
            g = (pack & 0x0000FF00) >> 8
            b = (pack & 0x000000FF)
            buffer.append(struct.pack('ffffBBBBIII', data[0], data[1], data[2], 1.0, b, g, r, 0, 0, 0, 0))

        ros_msg.data = b"".join(buffer)

        return ros_msg


if __name__ == "__main__":
    rospy.init_node('RGBD_point_filtering')
    handler = RGBD_handler()
    rospy.spin()
    
    
