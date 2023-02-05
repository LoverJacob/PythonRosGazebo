#!/usr/bin/env
import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
bridge = CvBridge()

def talk_to_me():
    pub = rospy.Publisher("open_topic", Image, queue_size=10)
    rospy.init_node("open_publisher_node", anonymous=True)
    rate = rospy.Rate(1)
    rospy.loginfo("Publisher Node Started, now publishing messeges")
    while not rospy.is_shutdown():
        msg = cv2.imread("/home/jakub/pythonopencv/src/package1/zdj/bruce.jpg",0)
        pub.publish(bridge.cv2_to_imgmsg(msg))
        rate.sleep()
if __name__ == "__main__":
    try:
        talk_to_me()
    except rospy.ROSInterruptException:
        pass



