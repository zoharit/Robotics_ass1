#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
import cv2
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
import sys


def webcam_pub():
    pub = rospy.Publisher('webcam/image_raw', Image, queue_size=1)
    rospy.init_node('webcam_pub', anonymous=True)
    rate = rospy.Rate(60) # 60hz
    cam = cv2.imread("colors.jpg")
    bridge = CvBridge()
    while not rospy.is_shutdown():
        msg = bridge.cv2_to_imgmsg(cam, encoding="bgr8")
	rospy.loginfo(' Publishing image')
        pub.publish(msg)
	rate.sleep()


if __name__ == '__main__':
    try:
        webcam_pub()
    except rospy.ROSInterruptException:
    	pass
