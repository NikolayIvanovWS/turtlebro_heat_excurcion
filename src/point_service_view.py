#!/usr/bin/env python3

from turtlebro_patrol.srv import PatrolPointCallback, PatrolPointCallbackRequest, PatrolPointCallbackResponse 
from turtlebro_heat_excursion.srv import ArucoDetect, ArucoDetectResponse, ArucoDetectRequest
from rospy.topics import Publisher
from std_msgs.msg import Float32MultiArray, String, Bool
import rospy
import subprocess
import numpy as np
import subprocess
import math


def __init__(self):
        self.current_max_temp = 0
        rospy.Subscriber('limit_switch', Bool, self.callback)
        self._heat_sub = rospy.Subscriber('amg88xx_pixels', Float32MultiArray, self.heat_callback)

def heat_callback(self, heat_msg):
    rospy.loginfo('HeatSensor: heat pixels message received')
    self.current_max_temp = np.max(heat_msg.data)
    rospy.loginfo('Current tempurature: %s', self.current_max_temp)

def callback (self, msg):
    if msg.data:
        temp_2 = int((self.current_max_temp-math.floor(self.current_max_temp))* 10.0)
        temp_1 = int(self.current_max_temp - temp_2/10.0)
        self.say_text("Ваша температура: " + str(temp_1) + " и " + str(temp_2))

    else:
        pass

def say_text(text):    
    rospy.loginfo(f"Start speech: {text}")
    subprocess.call('echo '+text+'|festival --tts --language russian', shell=True)
    rospy.loginfo("Speech end")

def handle_request(req:PatrolPointCallbackRequest):

    point_name = req.patrol_point.name
    
    text = "Местоположение неизвестно"
    
    if point_name == "1":
        text = "Я в точке 1"

    if point_name == "2":
        text = "Я в точке 2"

    if point_name == "home":
        text = "Я дома"

    aruco_result = aruco_detect.call(ArucoDetectRequest())

    if aruco_result.id > 0:
        text += f". Вижу маркер {aruco_result.id}"
    else : 
        text += ". Маркер не обнаружен"    

    say_text(text)

    return PatrolPointCallbackResponse(1, "Speech end")


rospy.init_node('excursion_point_service')
s = rospy.Service('turtlebro_heat_excursion', PatrolPointCallback, handle_request)
aruco_detect = rospy.ServiceProxy('aruco_detect', ArucoDetect)
rospy.loginfo("Ready to speak points")
rospy.spin()
