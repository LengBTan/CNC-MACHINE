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

#Global variables accessed by all functions
global xCoord
global yCoord
global zCoord
xCoord = 0
yCoord = 0
zCoord = 0

#Declare instance of a class to pass GPIO pins to RpiMotorLib library
yMotor = RpiMotorLib.BYJMotor("MyMotorOne", "Nema")
xMotor = RpiMotorLib.BYJMotor("MyMotorTwo", "Nema")
zMotor = RpiMotorLib.BYJMotor("MyMotorThree", "Nema")
time.sleep(0.5)


# Home function. This homes the X, Y and Z
# motors and stores the origin point as (0,0,0)
# Three limit switches are used to home each axes.
def home():
    global xCoord
    global yCoord
    global zCoord    
    ySwitch=Button(2) # gpio2 pin
    xSwitch=Button(3) # gpio3 pin
    zSwitch=Button(4) # gpio4 pin
    ySwitchIsPressed = False #stores boolean, tells the axes limit switches that they are not pressed
    xSwitchIsPressed = False
    zSwitchIsPressed = False
    while ((ySwitchIsPressed == False)) : # continuously checks if the limit switch is pressed. Moves the motor if the limit switch is not pressed
        if(ySwitch.is_pressed): # checks if limit switch is pressed, and sets the SwitchIsPressed to true, and sets the coordinates to the origin, else it moves the motor.
            print("y homed")
            ySwitchIsPressed = True
            yCoord = 0
        else:
            #time.sleep(.1)
            yMotor.motor_run(GPIOY_pins , 0.01, 1, True, False, "full", .05)

    while ((xSwitchIsPressed == False)):
        if(xSwitch.is_pressed):
            print("x homed")
            xSwitchIsPressed = True
            xCoord = 0
        else:
            #time.sleep(.1)
            xMotor.motor_run(GPIOX_pins, 0.01, 1, True, False , "full", .05)

    while ((zSwitchIsPressed == False)):
        if(zSwitch.is_pressed):
            print("z homed")
            zSwitchIsPressed = True
            zCoord = 0
        else:
            #time.sleep(.1)
            zMotor.motor_run(GPIOZ_pins , 0.01, 1, True, False, "full", .05)
    print("sucessfully homed")


# Move function. It moves the three diffrent axes of the CNC machine.
# pos1 parameter is the current coordinate for the motor at the specified axis.
# pos2 parameter is the next coordinate the motor will move to for the specified axis.
def moveX(pos1, pos2):
    global xCoord
    if(pos1 < pos2): #checks if pos1 is smaller than pos2 and finds the diffrence between pos2 and pos1.
        finalPos = pos2 - pos1 # stores the steps needed to move to the final coordinate
        xCoord = pos1 + finalPos # stores the current x coordinate 
        xMotor.motor_run(GPIOX_pins, 0.01, finalPos, False, False , "full", .05)
        print((finalPos), " CW X MOTOR")
    if(pos1 > pos2): # checks if pos1 is larger than pos2 and finds the diffrence between pos1 and pos2
        finalPos = pos1 - pos2
        xCoord = pos1 - finalPos
        xMotor.motor_run(GPIOX_pins, 0.01, finalPos, True, False , "full", .05)
        print((finalPos), " CCW X MOTOR")

def moveY(pos1, pos2):
    global yCoord
    if(pos1 < pos2):
        finalPos = pos2 - pos1
        yCoord = pos1 + finalPos
        yMotor.motor_run(GPIOY_pins , 0.01, finalPos, False, False, "full", .05)
        print((finalPos), " CW Y MOTOR")
    if(pos1 > pos2):
        finalPos = pos1 - pos2
        yCoord = pos1 - finalPos
        yMotor.motor_run(GPIOY_pins , 0.01, finalPos, True, False, "full", .05)
        print((finalPos), " CCW Y MOTOR")

def moveZ(pos1, pos2):
    global zCoord
    if(pos1 < pos2):
        finalPos = pos2 - pos1
        zCoord = pos1 + finalPos
        zMotor.motor_run(GPIOZ_pins , 0.01, finalPos, False, False, "full", .05)
        print((finalPos), " CW Z MOTOR")
    if(pos1 > pos2):
        finalPos = pos1 - pos2
        zCoord = pos1 - finalPos
        zMotor.motor_run(GPIOZ_pins , 0.01, finalPos, True, False, "full", .05)
        print((finalPos), " CCW Z MOTOR")


# Draw function. It opens a file containing coordinates for the 3 motor axes to move to.
# filename parameter stores the user entered filename, and reads it using open().
# It checks whether the x,y or z motor needs to move.
def draw(filename):
    f = open(filename, "r") #opens file
    data = f.read() #reads file
    lines = data.splitlines() # splits the lines into seperate strings
    home()
    for i,line in enumerate(lines): #reads each line to the end of the file
        if "X" in line: # checks if X is in the line
            xNext = int(line[1:])
            #print(i,xNext)
            moveX(xCoord, xNext)
        if "Y" in line: # checks if Y is in the line
            yNext = int(line[1:])
            #print(i,yNext)
            moveY(yCoord, yNext)
        if "Z" in line: # checks if Z is in the line
            zNext = int(line[1:])
            #print(i,zNext)
            moveZ(zCoord, zNext)
    f.close


# main function
if __name__ == "__main__":
    #home()
    while True: #loop
        filename = input("input: ")
        try: # Attempts to read filename using the draw function, if unable, prompts user that it could not load the file. 
            draw(filename)
        except IOError:
            print("Could not find or load file")

#GPIO.cleanup()
sys.exit() 