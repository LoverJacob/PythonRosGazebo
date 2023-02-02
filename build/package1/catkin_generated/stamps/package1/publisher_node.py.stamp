#!/usr/bin/env
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
def talk_to_me():
    pub = rospy.Publisher("talking_topic", String, queue_size=10)
    rospy.init_node("publisher_node", anonymous=True)
    rate = rospy.Rate(1)
    rospy.loginfo("Publisher Node Started, now publishing messeges")
    while not rospy.is_shutdown():
        msg = "Hello - %s" %rospy.get_time()
        pub.publish(msg)
        rate.sleep()
if __name__ == "__main__":
    try:
        talk_to_me()
    except rospy.ROSInterruptException:
        pass



