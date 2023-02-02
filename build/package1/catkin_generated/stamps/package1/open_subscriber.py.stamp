#!/usr/bin/env python2.7
  # Import ROS libraries and messages
import rospy
from sensor_msgs.msg import Image

  # Import OpenCV libraries and tools
import cv2
from cv_bridge import CvBridge, CvBridgeError



rospy.init_node('opencv_example', anonymous=True)

rospy.loginfo("Hello ROS!")

# Initialize the CvBridge class
bridge = CvBridge()

  # Define a function to show the image in an OpenCV Window
def show_image(img):
      cv2.imshow("Image Window", img)
      cv2.waitKey(3)

  # Define a callback for the Image message
def image_callback(img_msg):
      # log some info about the image topic
      rospy.loginfo(img_msg.header)

      # Try to convert the ROS Image message to a CV2 Image
      try:
        cv_image = bridge.imgmsg_to_cv2(img_msg, "passthrough")
      except rospy.ROSInterruptException:
        pass

      # Flip the image 90deg
      cv_image = cv2.transpose(cv_image)
      cv_image = cv2.flip(cv_image,1)

      # Show the converted image
      show_image(cv_image)

  # Initalize a subscriber to the "/camera/rgb/image_raw" topic with the function "image_callback" as a callback
sub_image = rospy.Subscriber("open_topic", Image, image_callback)
i=0
  # Initialize an OpenCV Window named "Image Window"
cv2.namedWindow("Image Window", 1)
sub_image = rospy.Subscriber("/home/jakub/pythonopencv/src/package1/zdj/chuck", Image, image_callback)

  # Loop to keep the program from shutting down unless ROS is shut down, or CTRL+C is pressed
while not rospy.is_shutdown():
#    if i==0:
#        sub_image = rospy.Subscriber("/home/jakub/pythonopencv/src/package1/zdj/chuck", Image, image_callback)
#        i=i+1
#    else:
#        i=0
#        sub_image = rospy.Subscriber("/home/jakub/pythonopencv/src/package1/zdj/bruce", Image, image_callback)
    rospy.spin()