#!/usr/bin/env python
# license removed for brevity

import rospy
import random
import tf
import math

import sys, getopt
from optparse import OptionParser


from geometry_msgs.msg import Twist


def follow(name,target,frame='base_footprint',speed=4,follow=True):
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rospy.init_node('name', anonymous=True)
    listener = tf.TransformListener()
    r = rospy.Rate(5) # 10hz
    r.sleep()
    #random.seed()
    if follow:
        rospy.loginfo("Intializing follow behavior")
    else:
        rospy.loginfo("Intializing flee behavior")
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform(name+'/'+frame, target+'/'+frame, rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException) as inst:
            #rospy.loginfo(inst)
            continue
        cmd = Twist()
        cmd.linear.x = 4 #drive with static speed
        if follow:
            cmd.angular.z = 7 * math.atan2(trans[1], trans[0])
        else:
            cmd.angular.z = - 7 * math.atan2(trans[1], trans[0])
        pub.publish(cmd)
        r.sleep()

if __name__ == '__main__':
    parser = OptionParser('usage: %prog [options] name target')
    #parser.add_option("-n", "--name", dest="name", action="store", type="string",
                  #help="Namespace of the robot", metavar="NAME")
    #parser.add_option("-t", "--target", dest="target",action="store", type="string",
                  #help="Namespace of the target robot", metavar="TARGET")
    parser.add_option("-e", "--flee", action="store_false", dest="follow",
                  help="Set the robot to flee mode")
    parser.add_option("-f", "--follow", action="store_true", dest="follow",
                  help="Set the robot to follow mode(default)", default=True)
    parser.add_option("-r", "--ref-frame", dest="frame", action="store", type="string",
                  help="reference frame default 'base_footprint'", default='base_footprint')

    (options, args) = parser.parse_args()
    
    print(len(args))
    try:
        follow(args[0],args[1],frame=options.frame,follow=options.follow)
    except rospy.ROSInterruptException: pass