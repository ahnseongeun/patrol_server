#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from owayeol.msg import Trigger
def talker():
    rospy.Publisher('/trigger', Trigger, queue_size=10)
    pub = rospy.Publisher('/trigger', Trigger, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) 
    while not rospy.is_shutdown():
        object_str =  "person"
        print(object_str)
        pub.publish(object_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
