# ass1_rob

Robotics with Ros Operating System and Catkin_Ws workspace-

In this program i build four nodes :

(1)The first node will use OpenCV to read the attached image -colors.jpg, and publish it on a topic. 

(2)The second node will be used to read a color from the input, and publish it on a topic. 

(3)The third node will subscribe to both topics, receive the image and the color, find the coordinates for the center of the circle with this color and it’s radius. The coordinates will be advertised on a new topic. 

(4)The last node will receive the coordinates and radius, recieve the image from the first topic, draw a circle around the circle of the selected color and save the new image to a file. 

In order to use it install ROS OS & Catkin_Ws at: http://wiki.ros.org/ROS/Installation

## Running instructions:
* $source /opt/ros/kinetic/setup.bash
* $source devel/setup.bash
* $roscore
* $catkin_make
* $rosrun beginner_tutorials node1.py
* $rosrun beginner_tutorials node2.py r g b
* $rosrun beginner_tutorials node3.py
* $rosrun beginner_tutorials node4.py

## R-G-B Exampls:
* red: 255 0 0
* green: 0 255 0
* blue: 0 0 255
* yellow: 255 255 0
* purple: 130 0 130

