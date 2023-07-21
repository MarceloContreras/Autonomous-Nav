#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import PointCloud2
from pcl_helpers import *
from tf_helpers import *
from geometry_msgs.msg import Transform,TransformStamped
import tf2_ros

class RGBD_handler(object):
    def __init__(self):
        self.sub = rospy.Subscriber('/filtered_dense',PointCloud2,self.callback,queue_size=50)
        self.pub = rospy.Publisher('/transform_dense',PointCloud2,queue_size=50)
        self.tf  = tf.TransformListener()

    def callback(self,msg):
        (trans, rot) = self.tf.lookupTransform('map','camera_rgb_optical_frame',rospy.Time(0))
        T_mat = TransformStamped()
        T_mat.transform.translation.x = trans[0]
        T_mat.transform.translation.y = trans[1]
        T_mat.transform.translation.z = trans[2]
        T_mat.transform.rotation.x = rot[0]
        T_mat.transform.rotation.y = rot[1]
        T_mat.transform.rotation.z = rot[2]
        T_mat.transform.rotation.w = rot[3]
        new_points = do_transform_cloud(msg,T_mat)
        new_points.header.frame_id = 'map'
        self.pub.publish(new_points)

if __name__ == "__main__":
    rospy.init_node('Point_transform')
    handler = RGBD_handler()
    rospy.spin()