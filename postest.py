
from io import StringIO

#Global variables
global xCoord
global yCoord
global zCoord
xCoord = 0
yCoord = 0
zCoord = 0


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

def startdraw(filename):
    f = open(filename, "r")
    data = f.read()
    lines = data.splitlines()
    for i,line in enumerate(lines):
        if "X" in line:
            xNext = int(line[1:])
            moveX(xCoord, xNext)
            #print(xNext)
        if "Y" in line:
            yNext = int(line[1:])
            moveY(yCoord,yNext)
            #print(yNext)
        if "Z" in line:
            zNext = int(line[1:])
            moveZ(zCoord,zNext)
            #print(zNext)
    f.close


if __name__ == "__main__":
    while True:
        filename = input("input: ")
        xCoord = 0 #home
        try:
            startdraw(filename)
        except IOError:
            print("Could not find or load file")
        