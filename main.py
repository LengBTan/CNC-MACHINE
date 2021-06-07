import sys
import time
import threading
import gpiozero
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
YMotor = RpiMotorLib.BYJMotor("MyMotorOne", "Nema")
XMotor = RpiMotorLib.BYJMotor("MyMotorTwo", "Nema")
ZMotor = RpiMotorLib.BYJMotor("MyMotorThree", "Nema")
time.sleep(0.5)

#YMotor.motor_run(GPIOY_pins , 0.005, 60, False, True, "half", .05)
#YMotor.motor_run(GPIOY_pins , 0.005, 60, True, True, "half", .05)

#XMotor.motor_run(GPIOX_pins , 0.005, 60, False, False, "half", .05)
#XMotor.motor_run(GPIOX_pins , 0.005, 60, True, False, "half", .05)

#ZMotor.motor_run(GPIOZ_pins , 0.005, 60, False, False, "half", .05)
#ZMotor.motor_run(GPIOZ_pins , 0.005, 60, True, False, "half", .05)

def home():
    ySwitch = False
    xSwitch = False
    zswitch = False
    while ySwitch == False :
        ##YMotor.motor_run(GPIOY_pins , 0.005, 10, False, True, "half", .05)
        if(ySwitch==True):
            print("homed")
            break



GPIO.cleanup()
sys.exit() 