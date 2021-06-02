import time
import gpiozero
from RpiMotorLib import RpiMotorLib

GPIO_pins=(14,15,18,23)

mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "yMotor")
time.sleep(0.5)

mymotortest.motor_run(GPIO_pins , 0.1, 50, False, False, "half", .05)


