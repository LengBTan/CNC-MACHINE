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

xCoord = 0
yCoord = 0
zCoord = 0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


GPIO.setup(GPIOX_pins[0],GPIO.OUT)
GPIO.setup(y_endstop_pin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

#Declare instance of a class to pass GPIO pins to RpiMotorLib
yMotor = RpiMotorLib.BYJMotor("MyMotorOne", "Nema")
xMotor = RpiMotorLib.BYJMotor("MyMotorTwo", "Nema")
zMotor = RpiMotorLib.BYJMotor("MyMotorThree", "Nema")
time.sleep(0.5)

def home():
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

<<<<<<< HEAD
=======
    while ((xSwitchIsPressed == False)) :
>>>>>>> a36d1083529cf4f97b8213537d659c313e6a178e
        if(xSwitch.is_pressed):
            print("x homed")
            xSwitchIsPressed = True
        else:
            print("xmotortest")
            time.sleep(1)
            #yMotor.motor_run(GPIOY_pins , 0.005, 60, False, True, "half", .05)

<<<<<<< HEAD
=======
    while ((zSwitchIsPressed == False)) :
>>>>>>> a36d1083529cf4f97b8213537d659c313e6a178e
        if(zSwitch.is_pressed):
            print("z homed")
            zSwitchIsPressed = True
        else:
            print("zmotortest")
            time.sleep(1)
            #yMotor.motor_run(GPIOY_pins , 0.005, 60, False, True, "half", .05)
    print("sucessfully homed")


def moveYAxis():
    print("")
def moveXAxis():
    print("")
def moveZAxis():
    print("")



GPIO.cleanup()
sys.exit() 