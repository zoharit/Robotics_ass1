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
    global r
    global g
    global b
    r=data.r
    g=data.g
    b=data.b
    
    rospy.loginfo(rospy.get_caller_id() + "I heard "+str(data.r)+str(data.g)+str(data.b)+str(data.a)) 
    if not (data) == None:
	    image_sub = rospy.Subscriber("webcam/image_raw",Image,callback1)
   
 
def pub(radius , x,y):
    publisher = rospy.Publisher('/radius/', Twist, queue_size=10)
    rate=rospy.Rate(0.2)
    vel_msg = Twist()
    vel_msg.linear.x=radius
    vel_msg.linear.y=x
    vel_msg.linear.z=y
    while not rospy.is_shutdown():
        rospy.loginfo('Publishing')
        publisher.publish(vel_msg)
        rate.sleep()


def callback1(data):
  try:
   cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
  except CvBridgeError as e:
    print(e)
  (rows,cols,channels) = cv_image.shape
  if cols > 60 and rows > 60 :
    cv2.circle(cv_image, (50,50), 10, 255)
  #cv2.imshow("Image window", cv_image)
  r1 ,g1,b1=colorsys.rgb_to_hsv(r,g,b)
  red = np.uint8([[[b,g,r ]]])
  redHSV = cv2.cvtColor(red, cv2.COLOR_BGR2HSV) 
  greenLower = (redHSV[0][0][0]-25, 50, 50)
  greenUpper = (redHSV[0][0][0]+25, 255, 255)
  
  height, width, channels = cv_image.shape
  blurred = cv2.GaussianBlur(cv_image, (11, 11), 0)
  hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
  mask = cv2.inRange(hsv, greenLower, greenUpper)
  mask = cv2.erode(mask, None, iterations=2)
  mask = cv2.dilate(mask, None, iterations=2)
  (_,cnts, _)  = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
  center = None
  if len(cnts) > 0:
  	c = max(cnts, key=cv2.contourArea)
  	((x, y), radius) = cv2.minEnclosingCircle(c)
	M = cv2.moments(c)
	center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
  pub(radius, x,y)
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('/ledscape_ros/array', ColorRGBA, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()




