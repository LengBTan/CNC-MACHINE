import sys
import time
import threading
from gpiozero import Button
from RpiMotorLib import RpiMotorLib

ySwitch=Button(2)
xSwitch=Button(3)
zSwitch=Button(4)
ySwitchIsPressed = False
xSwitchIsPressed = False
zSwitchIsPressed = False
while ((ySwitchIsPressed == False)) :
    if(ySwitch.is_pressed):
        print("y homed")
        ySwitchIsPressed = True
    else:
        print("ymotortest")
        time.sleep(1)
        #yMotor.motor_run(GPIOY_pins , 0.005, 60, False, True, "half", .05)

while ((xSwitchIsPressed == False)) :
    if(xSwitch.is_pressed):
        print("x homed")
        xSwitchIsPressed = True
    else:
        print("xmotortest")
        time.sleep(1)
        #yMotor.motor_run(GPIOY_pins , 0.005, 60, False, True, "half", .05)

while ((zSwitchIsPressed == False)) :
    if(zSwitch.is_pressed):
        print("z homed")
        zSwitchIsPressed = True
    else:
        print("zmotortest")
        time.sleep(1)
        #yMotor.motor_run(GPIOY_pins , 0.005, 60, False, True, "half", .05)
print("sucessfully homed")