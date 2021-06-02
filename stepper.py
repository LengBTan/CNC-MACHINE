import sys
import time
import gpiozero
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

GPIO_pins=(14,15,18,23)

mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "yMotor")
time.sleep(0.5)

mymotortest.motor_run(GPIO_pins , 0.01, 20, False, True, "half", .05)
mymotortest.motor_run(GPIO_pins , 0.01, 30, True, True, "half", .05)

GPIO.cleanup()

