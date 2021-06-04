from stepper import GPIOX_pins, GPIOY_pins, GPIOZ_pins
import sys
import time
import gpiozero
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

GPIOY_pins=()
GPIOX_pins=()
GPIOZ_pins=()

# Declare instance of a class to pass GPIO pins to RpiMotorLib
# 3rd input is for microstep resolution for the A4988, which is not needed as it is hardwired.
MyMotorY = RpiMotorLib.A4988(GPIOY_pins[0],GPIOY_pins[1],(-1,-1,-1), "A4988") 
MyMotorX = RpiMotorLib.A4988(GPIOX_pins[0],GPIOX_pins[1],(-1,-1,-1), "A4988")
MyMotorZ = RpiMotorLib.A4988(GPIOZ_pins[0],GPIOZ_pins[1],(-1,-1,-1), "A4988")

MyMotorY.motor_go(True,"Half",60, 0.1,False,0.05)
MyMotorY.motor_go(False,"Half",60, 0.1,False,0.05)


GPIO.cleanup()