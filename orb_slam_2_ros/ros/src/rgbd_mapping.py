#!/usr/bin/env python3
import rospy
import pcl
from sensor_msgs.msg import PointCloud2
from pcl_helpers import *

class RGBD_handler(object):
    def __init__(self):
        self.sub = rospy.Subscriber('/orb_slam2_rgbd/map_points',PointCloud2,self.callback,queue_size=50)
        self.pub = rospy.Publisher('/filtered_RGBD',PointCloud2,queue_size=50)
        self.VOXEL_SIZE = 0.01
        self.SCALE_FACTOR = 1.0

    def callback(self,msg):
        plc_cloud   = ros_to_pcl(msg)
        plc_cloud   = self.filter_downsampling(plc_cloud)
        plc_cloud   = self.filter_kmeans(plc_cloud)
        ros_filteredcloud = pcl_to_ros(XYZ_to_XYZRGB(plc_cloud,[255,255,255]))
        self.pub.publish(ros_filteredcloud)
    
    def filter_downsampling(self,point_cloud):
        fvox = point_cloud.make_voxel_grid_filter()
        fvox.set_leaf_size(self.VOXEL_SIZE, self.VOXEL_SIZE, self.VOXEL_SIZE)
        pcl_downsampled = fvox.filter()
        return pcl_downsampled
    
    def filter_kmeans(self,point_cloud):
        outlier_filter = point_cloud.make_statistical_outlier_filter()
        outlier_filter.set_mean_k(5)
        outlier_filter.set_std_dev_mul_thresh(self.SCALE_FACTOR)
        cloud_filtered = outlier_filter.filter()
        return cloud_filtered


if __name__ == "__main__":
    rospy.init_node('RGBD_point_filtering')
    handler = RGBD_handler()
    rospy.spin()
    
