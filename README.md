# Manual for 
turtlebro_heat_excurcion

### Required equipment

TurtleBro
AMG88xx thermal sensor
Limit switch
Audio speakers

### Description

This package allows you to start different nodes for excursion.

Node "heat_sensor" allows TurtleBro to receive data from the AMG88xx GridEYE 8x8 IR camera thermal sensor. When a heat source with a temperature higher than threshold (you can configure this param in the launch file) is detected, the detection node sends True into /heat_sensor_output topic.

Node "aruco_detect_server" allows TurtleBro to work with the videostream from camera and recognize aruco marker.

Node "heat_speaker" allows TurtleBro to speak the measured temperature and control the excursion. 

Node "excursion_point_service" allows TurtleBro to implement a function in which the robot recognize and speak aruco markers


### Connecting thermal sensor

AMG88xx thermal sensor   must be connected to built-in arduino compatible controller via I2C protocol. Wires from AMG88XX pins must be connected to one of the white connectors A8-A11 or A13-A15 on the TurtleBoard.

Sensor documentation:  
https://cdn.sparkfun.com/assets/4/1/c/0/1/Grid-EYE_Datasheet.pdf  
https://cdn-learn.adafruit.com/downloads/pdf/adafruit-amg8833-8x8-thermal-camera-sensor.pdf  

Wiring:  

AMG88XX pins -> Turtlebro pin  
VIN -> 5V  
GND -> GND  
SDA -> SDA  
SCL -> SCL  

Example about connecting AMG88xx to Arduino:  
https://learn.adafruit.com/adafruit-amg8833-8x8-thermal-camera-sensor/arduino-wiring-test  


### Connecting limit switch

Limit switch 'NC' pin must be connected STRICTLY to pin marked 'GPIO' in  white connector marked as 'A12'.   
Limit switch 'GND' pin must be connected to 'GND' pin on the same connector marked as 'A12'.  
Limit switch 'VCC' pin must be connected to '5V' pin on the same connector marked as 'A12'.  

### Connecting audio speakers

To mount the speaker, install the upper mounting pad on the robot. Next, install the speaker according to the configuration. Connect the speaker as follows:

The USB cable of the speaker -> to the USB port of the Raspberry Pi
Speaker Audio Cable -> to Raspberry Pi Audio Port

### How to install on Arduino

Install Arduino IDE https://www.arduino.cc/en/main/software  
 - Open the Arduino Library Manager, find AMGXX library in search string, and install it. You also can download it directly from https://github.com/adafruit/Adafruit_AMG88xx  

 - Generate and copy ros_lib to your Arduino Libraries.

 - Open file src/arduino/amg88xx_lm_main.ino from cloned repo in Arduino IDE.
Connect built-in turtlebro`s Arduino Mega via USB, and upload script to it.
(or upload remotely)

After uploading you must see topics "/amg88xx_pixels" and "/limit_switch" in list of ros topics.

### Package installation

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

### Launching

Before launch you have to clear data from stm32 by sending reset command:

```
rosservice call /reset
```

```
roslaunch turtlebro_heat_excursion heat_excursion.launch
```


