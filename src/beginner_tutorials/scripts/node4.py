#!/usr/bin/env python
import rospy
from std_msgs.msg import ColorRGBA
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
bridge = CvBridge()
import cv2
import colorsys
from geometry_msgs.msg import Twist

def callback(data):
    global radius
    global x
    global y
    radius=data.linear.x
    x=data.linear.y
    y=data.linear.z
    rospy.loginfo(rospy.get_caller_id() + "I heard "+str(data.linear.x)+str(data.linear.y)+str(data.linear.z)) 
    if not (data) == None:
	    image_sub = rospy.Subscriber("webcam/image_raw",Image,callback1)

def callback1(data):
  try:
   cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
  except CvBridgeError as e:
    print(e)
  (rows,cols,channels) = cv_image.shape
  if cols > 60 and rows > 60 :
    cv2.circle(cv_image, (50,50), 10, 255)
  cv2.circle(cv_image,(int(x),int(y)), int(radius), (0,255,0), 3,30,0)
  cv2.imwrite('../Desktop/colors_copy.jpg', cv_image) 
  cv2.imshow("Image.jpg", cv_image)
  cv2.waitKey(0)
  cv2.destroyAllWindows() 

def listener():


    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener1', anonymous=True)
    rospy.Subscriber('/radius/', Twist, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()




