#! /usr/bin/env python3

"""
voltbro 2020
"""

import rospy
import numpy as np
from std_msgs.msg import Float32MultiArray, String, Bool

class HeatSensor(object):
    """
    it can receive message from heat sensor topic in form of 64x1 Float32MultiArray
    """

    def __init__(self):

        self._current_pixel_array = None
        self._heat_pixels_topic = 'amg88xx_pixels' 
        self._output_topic = 'heat_sensor_output'

        rospy.init_node('heat_sensor')
        rospy.loginfo('HeatSensor: start heat detector node')

        # get roslaunch params and reinit part of params
 
        self._threshold = rospy.get_param('~threshold', 55)

        self._heat_pixels_topic = rospy.get_param('~heat_pixels_topic', 'amg88xx_pixels')

        self._rate = rospy.Rate(10)

        self._current_max_temp = None
        # init self as subscriber and publisher and start node

        self._heat_sub = rospy.Subscriber(self._heat_pixels_topic, Float32MultiArray, self._heat_callback)
        self._output_pub = rospy.Publisher(self._output_topic, Bool, queue_size=10)

    def _max_detector(self):
        """
        If one pixel from data array is bigger than threshold, then panic
        """
        self._current_max_temp = np.max(self._current_pixel_array)

        if self._current_max_temp >= self._threshold:
            self._output_pub.publish(True)
        else:
            self._output_pub.publish(False)


    def _heat_callback(self, heat_msg):
        # just put msg data to self variable
        self._current_pixel_array = heat_msg.data
        self._max_detector()
        rospy.loginfo('HeatSensor: heat max value is {}'.format(np.max(self._current_pixel_array)))

    def main (self):
        pass



hd = HeatSensor()

while not rospy.is_shutdown():
    rospy.sleep(0.1)
    hd.main()
