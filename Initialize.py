import sys
import time
import gpiozero
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

GPIOY_pins=(14,15,18,23)
GPIOX_pins=(24,25,8,7)
GPIOZ_pins=(1,12,16,20)

GPIO.output =(GPIOY_pins[0],0)
GPIO.output =(GPIOY_pins[1],0)
GPIO.output =(GPIOY_pins[2],0)