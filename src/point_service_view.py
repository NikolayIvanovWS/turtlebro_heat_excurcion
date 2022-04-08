#!/usr/bin/env python3

"""
voltbro 2022
"""

from turtlebro_patrol.srv import PatrolPointCallback, PatrolPointCallbackRequest, PatrolPointCallbackResponse 
from turtlebro_heat_excursion.srv import ArucoDetect, ArucoDetectResponse, ArucoDetectRequest
import rospy
import subprocess

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
