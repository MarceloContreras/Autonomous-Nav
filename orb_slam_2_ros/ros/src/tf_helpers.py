#!/usr/bin/env python3
import rospy
import numpy as np
import tf
from tf2_sensor_msgs.tf2_sensor_msgs import do_transform_cloud

def rotFromQuat(q):
  """ q = [ex, ey, ez, ew]
  """
  return np.array([[2.*(q[3]**2+q[0]**2)-1., 2.*(q[0]*q[1]-q[3]*q[2]), 2.*(q[0]*q[2]+q[3]*q[1])],
                   [2.*(q[0]*q[1]+q[3]*q[2]), 2.*(q[3]**2+q[1]**2)-1., 2.*(q[1]*q[2]-q[3]*q[0])],
                   [2.*(q[0]*q[2]-q[3]*q[1]), 2.*(q[1]*q[2]+q[3]*q[0]), 2.*(q[3]**2+q[2]**2)-1.]])


def transformPointCloud(points):
  """
  Sistema del lidar con respecto a base_footprint
  """
  tflistener = tf.TransformListener()
  T          = np.eye(4)
  new_points = None
  rospy.sleep(5e-4)
  try:
    #(trans, rot) = tflistener.lookupTransform('map', 'camera_rgb_optical_frame', rospy.Time(0))
    #T[0:3,0:3] = rotFromQuat(rot)
    #T[0:3,3] = trans
    trans = tflistener.lookupTransform('map','camera_rgb_optical_frame',rospy.Time(0))
    print(trans)
    new_points = do_transform_cloud(points,trans)
  except:
    pass

  return new_points

