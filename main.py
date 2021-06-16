#import libraries and packages
import sys
import time
import threading
from gpiozero import Button
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
from io import StringIO


#setup GPIO pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIOY_pins=[14,15,18,23]
GPIOX_pins=[24,25,8,7]
GPIOZ_pins=[1,12,16,20]

x_endstop_pin = 2
y_endstop_pin = 3
z_endstop_pin = 4

#Global variables
global xCoord
global yCoord
global zCoord
xCoord = 0
yCoord = 0
zCoord = 0

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
            time.sleep(.1)
            yMotor.motor_run(GPIOY_pins , 0.01, 1, True, False, "half", .05)

    while ((xSwitchIsPressed == False)):
        if(xSwitch.is_pressed):
            print("x homed")
            xSwitchIsPressed = True
        else:
            time.sleep(.1)
            xMotor.motor_run(GPIOX_pins, 0.01, 1, True, False , "half", .05)

    while ((zSwitchIsPressed == False)):
        if(zSwitch.is_pressed):
            print("z homed")
            zSwitchIsPressed = True
        else:
            time.sleep(.1)
            zMotor.motor_run(GPIOZ_pins , 0.01, 1, True, False, "half", .05)
    print("sucessfully homed")

def moveX(pos1, pos2):
    global xCoord
    if(pos1 < pos2):
        finalPos = pos2 - pos1
        xCoord = pos1 + finalPos
        print((finalPos), " CW X MOTOR")
    if(pos1 > pos2):
        finalPos = pos1 - pos2
        xCoord = pos1 - finalPos
        print((finalPos), " CCW X MOTOR")

def moveY(pos1, pos2):
    global yCoord
    if(pos1 < pos2):
        finalPos = pos2 - pos1
        yCoord = pos1 + finalPos
        print((finalPos), " CW Y MOTOR")
    if(pos1 > pos2):
        finalPos = pos1 - pos2
        yCoord = pos1 - finalPos
        print((finalPos), " CCW Y MOTOR")

def moveZ(pos1, pos2):
    global zCoord
    if(pos1 < pos2):
        finalPos = pos2 - pos1
        zCoord = pos1 + finalPos
        print((finalPos), " CW Z MOTOR")
    if(pos1 > pos2):
        finalPos = pos1 - pos2
        zCoord = pos1 - finalPos
        print((finalPos), " CCW Z MOTOR")

def draw(filename):
    f = open(filename, "r")
    data = f.read()
    lines = data.splitlines()
    for i,line in enumerate(lines):
        if "X" in line:
            xNext = line[1:]
            #print(xNext)
            moveX(xCoord, xNext)
        if "Y" in line:
            yNext = line[1:]
            #print(yNext)
            moveY(yCoord, yNext)
        if "Z" in line:
            zNext = line[1:]
            #print(zNext)
            moveZ(zCoord, zNext)
    f.close

if __name__ == "__main__":
    while True:
        filename = input("input")
        try:
            home()
            draw(filename)
        except IOError:
            print("Could not find or load file")

#GPIO.cleanup()
sys.exit() 