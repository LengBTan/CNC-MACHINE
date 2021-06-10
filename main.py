import sys
import time
import threading
from gpiozero import Button
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

GPIOY_pins=[14,15,18,23]
GPIOX_pins=[24,25,8,7]
GPIOZ_pins=[1,12,16,20]

x_endstop_pin = 2
y_endstop_pin = 3
z_endstop_pin = 4


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


GPIO.setup(GPIOX_pins[0],GPIO.OUT)
GPIO.setup(y_endstop_pin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

#Declare instance of a class to pass GPIO pins to RpiMotorLib
yMotor = RpiMotorLib.BYJMotor("MyMotorOne", "Nema")
xMotor = RpiMotorLib.BYJMotor("MyMotorTwo", "Nema")
zMotor = RpiMotorLib.BYJMotor("MyMotorThree", "Nema")
time.sleep(0.5)

#yMotor.motor_run(GPIOY_pins , 0.005, 60, False, True, "half", .05)
#yMotor.motor_run(GPIOY_pins , 0.005, 60, True, True, "half", .05)

#xMotor.motor_run(GPIOX_pins , 0.005, 60, False, False, "half", .05)
#xMotor.motor_run(GPIOX_pins , 0.005, 60, True, False, "half", .05)

#zMotor.motor_run(GPIOZ_pins , 0.005, 60, False, False, "half", .05)
#zMotor.motor_run(GPIOZ_pins , 0.005, 60, True, False, "half", .05)

def home():
    ySwitch=Button(2)
    xSwitch=Button(3)
    zSwitch=Button(4)
    ySwitchIsPressed = False
    xSwitchIsPressed = False
    zSwitchIsPressed = False
    while ((ySwitchIsPressed == False) and (xSwitchIsPressed == False) and (zSwitchIsPressed == False)) :
        if(ySwitch.is_pressed):
            print("y homed")
            ySwitchIsPressed = True
        else:
            print("ymotortest")
            #yMotor.motor_run(GPIOY_pins , 0.005, 60, False, True, "half", .05)

        if(xSwitch.is_pressed):
            print("x homed")
            xSwitchIsPressed = True
        else:
            print("xmotortest")
            #xMotor.motor_run(GPIOY_pins , 0.005, 60, False, True, "half", .05)

        if(zSwitch.is_pressed):
            print("z homed")
            zSwitchIsPressed = True
        else:
            print("zmotortest")
            #zMotor.motor_run(GPIOY_pins , 0.005, 60, False, True, "half", .05)





GPIO.cleanup()
sys.exit() 