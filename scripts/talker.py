#! /usr/bin/env python

import rospy
from std_msgs.msg import String

rospy.init_node('talker', anonymous = True)
pub = rospy.Publisher('my_chat_topic', String, queue_size=10)
rate = rospy.Rate(1)

def start_talker():
	msg = String()
	num = 0
	while not rospy.is_shutdown():
		hello_str = "%s" % num
		rospy.loginfo(hello_str)

		msg.data = hello_str
		pub.publish(msg)
		num = (num + 2) % 10 
		rate.sleep()

try:
	start_talker()
except (rospi.ROSInterruptException, KeyboardInterrupt):
	rospy.logger('Exception catched')