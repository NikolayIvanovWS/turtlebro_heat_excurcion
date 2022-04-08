# turtlebro_heat_excurcion

### Description

This package allows you to start different nodes for excursion.

Node "heat_sensor" allows TurtleBro to receive data from the AMG88xx GridEYE 8x8 IR camera thermal sensor. When a heat source with a temperature higher than threshold (you can configure this param in the launch file) is detected, the detection node sends True into /heat_sensor_output topic.

Node "aruco_detect_server" allows TurtleBro to work with the videostream from camera and recognize aruco marker.

Node "heat_speaker" allows TurtleBro to speak the measured temperature and control the excursion. 

Node "excursion_point_service" allows TurtleBro to implement a function in which the robot recognize and speak aruco markers

#### Package installation

First, you need to install turtlebro_patrol packade to TurtleBro:

```
cd ~/catkin_ws/src
git clone https://github.com/voltbro/turtlebro_patrol
cd ..
catkin_make --pkg turtlebro_patrol
```

After that, you can install turtlebro_heat_excurcion package:

```
cd ~/catkin_ws/src
git clone https://github.com/NikolayIvanovWS/turtlebro_heat_excurcion.git

cd ~/catkin_ws
catkin_make --pkg turtlebro_heat_excursion
```

#### Launching

Before launch you have to clear data from stm32 by sending reset command:

```
rosservice call /reset
```

```
roslaunch turtlebro_heat_excursion heat_excursion.launch
```


