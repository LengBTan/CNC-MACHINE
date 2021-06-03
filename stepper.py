import sys
import time
import gpiozero
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

GPIOY_pins=(14,15,18,23)
GPIOX_pins=(24,25,8,7)
GPIOZ_pins=(1,12,16,20)

mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "yMotor")
##mymotortest = RpiMotorLib.BYJMotor("MyMotorTwo", "xMotor")
##mymotortest = RpiMotorLib.BYJMotor("MyMotorThree", "zMotor")
time.sleep(0.5)

mymotortest.motor_run(GPIOY_pins , 0.005, 60, False, True, "half", .05)
mymotortest.motor_run(GPIOY_pins , 0.005, 60, True, True, "half", .05)

mymotortest.motor_run(GPIOX_pins , 0.005, 60, False, True, "half", .05)
mymotortest.motor_run(GPIOX_pins , 0.005, 60, True, True, "half", .05)

mymotortest.motor_run(GPIOZ_pins , 0.005, 60, False, True, "half", .05)
mymotortest.motor_run(GPIOZ_pins , 0.005, 60, True, True, "half", .05)

GPIO.cleanup()

sys.exit() 