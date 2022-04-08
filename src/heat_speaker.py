#!/usr/bin/env python3

"""
voltbro 2022
"""

from rospy.topics import Publisher
from std_msgs.msg import Float32MultiArray, String, Bool
import rospy
import numpy as np
import subprocess
import math


class RobotSpeaker():
    def __init__(self):
        self.current_max_temp = 0
        self.cmd_to_start = False
        rospy.init_node("heat_speaker")
            
        self._input_topic = 'excursion_control'
        self._patrol_topic = 'patrol_control'
        self._sensor_topic = 'amg88xx_pixels'
        self._button_topic = 'limit_switch'

        self._heat_sub = rospy.Subscriber(self._sensor_topic, Float32MultiArray, self._heat_callback)
        self._button_sub = rospy.Subscriber(self._button_topic, Bool, self._button_callback)
        self._input_sub = rospy.Subscriber(self._input_topic, String, self._input_callback)
        self._patrol_pub = rospy.Publisher(self._patrol_topic, String, queue_size=10)


    def _heat_callback(self, heat_msg):
        self.current_max_temp = np.max(heat_msg.data)

    def _button_callback (self, button_msg):
        if button_msg.data:
            rospy.loginfo('LimitSwitch: %s', button_msg.data) 
            temp_2 = int((self.current_max_temp-math.floor(self.current_max_temp))* 10.0)
            temp_1 = int(self.current_max_temp - temp_2/10.0)
            self.say_text("Ваша температура: " + str(temp_1) + " и " + str(temp_2) + " градусов")
            self._start_patrol()
        else:
            pass
        
    def _input_callback(self, msg):

        if msg.data == 'start':
            self.cmd_to_start = True

        elif msg.data == 'pause':
            self._pause_patrol()

        elif msg.data == 'resume':
            self._resume_patrol()

        elif msg.data == 'home':
            self._home_patrol()

        elif msg.data == 'stop':
            self._stop_patrol()
     

    def _start_patrol(self):
        if self.cmd_to_start:
            self._patrol_pub.publish('start')
            rospy.loginfo("Excursion command: start")
        else:
            pass        
        
    def _pause_patrol(self):
        self._patrol_pub.publish('pause')
        rospy.loginfo("Excursion command: pause")

    def _resume_patrol(self):
        self._patrol_pub.publish('resume')
        rospy.loginfo("Excursion command: resume")

    def _home_patrol(self):
        self._patrol_pub.publish('home')
        rospy.loginfo("Excursion command: home")

    def _stop_patrol(self):
        self._patrol_pub.publish('shutdown')
        rospy.loginfo("Excursion command: stop")

    def main (self):
        pass

    def say_text(self, text):    
        rospy.loginfo(f"Start speech: {text}")
        subprocess.call('echo '+text+'|festival --tts --language russian', shell=True)
        rospy.loginfo("Speech end") 

r = RobotSpeaker()

while not rospy.is_shutdown():
    rospy.sleep(0.1)
    r.main()