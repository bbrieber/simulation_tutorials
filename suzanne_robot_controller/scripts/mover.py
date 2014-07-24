#!/usr/bin/env python
# license removed for brevity

import rospy
import random


from geometry_msgs.msg import Twist


def mover():
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rospy.init_node('mover2', anonymous=True)
    r = rospy.Rate(5) # 10hz
    #random.seed()
    rospy.loginfo("Intializing controll module")
    while not rospy.is_shutdown():
        cmd = Twist()
        cmd.linear.x = -4
        cmd.angular.z = 3
        pub.publish(cmd)
        r.sleep()

if __name__ == '__main__':
    try:
        mover()
    except rospy.ROSInterruptException: pass