from ultralytics import YOLO
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

import message_filters
import rospy
import numpy as np

class ImageHandler(object):
  def __init__(self):
    self.bridge    = CvBridge()
    self.model     = YOLO('yolov8n.pt','v8')
    self.model.classes = [0] 
    self.img_sub   = message_filters.Subscriber("/camera/rgb/image_raw", Image)
    self.depth_sub = message_filters.Subscriber("/camera/depth/image_raw", Image)
    self.ts = message_filters.ApproximateTimeSynchronizer([self.img_sub,self.depth_sub],10,0.05)
    self.ts.registerCallback(self.callback)
    self.publisher = rospy.Publisher("/masked_depth",Image,queue_size = 10)

  def callback(self,img_msg,depth_msg):
    try:
        img_rgb   = self.bridge.imgmsg_to_cv2(img_msg)
        img_depth = self.bridge.imgmsg_to_cv2(depth_msg) 
    except CvBridgeError as e:
        print(e)
    
    results = self.model.predict(img_rgb, save=False, imgsz=320, conf=0.5)
    resultados = results[0].cpu().boxes.xyxy

    if (len(resultados) != 0):    
        x1 = int(resultados[0][0])
        y1 = int(resultados[0][1])
        x2 = int(resultados[0][2])
        y2 = int(resultados[0][3])
        img_depth_cropped = img_depth.copy()
        mask = np.ones(img_depth.shape, dtype=bool)
        mask[y1:y2,x1:x2] = False
        img_depth_cropped[mask] = 0
        
        msg = self.bridge.cv2_to_imgmsg(img_depth_cropped)
        msg.header.stamp = rospy.Time.now()

        self.publisher.publish(msg)
    	
###########     MAIN       ###############
if __name__ == '__main__':
    rospy.init_node('detection_node', anonymous=True)
    print('Creando nodo')
    image_handler = ImageHandler()
    rospy.spin()
