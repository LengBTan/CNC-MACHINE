
from io import StringIO

global xcoord
xcoord = 0

def move(pos1, pos2):
    global xcoord
    if(pos1 < pos2):
        finalPos = pos2 - pos1
        xcoord = pos1 + finalPos
        print((finalPos), " CW")
    if(pos1 > pos2):
        finalPos = pos1 - pos2
        xcoord = pos1 - finalPos
        print((finalPos), " CCW")


""" move(xcoord, pos1)
print("current coord is:", xcoord)
move(xcoord, pos2)
print("current coord is:", xcoord)
 """

def startdraw(filename):
    f = open(filename, "r")
    data = f.read()
    lines = data.splitlines()
    for i,line in enumerate(lines):
        if "X" in line:
            xNext = int(line[1:])
            move(xcoord, xNext)
            #print(xNext)
        if "Y" in line:
            yNext = int(line[1:])
            
            
            #print(yNext)
        if "Z" in line:
            zNext = int(line[1:])
            
            
            #print(zNext)
    f.close


if __name__ == "__main__":
    while True:
        filename = input("input: ")
        xcoord = 0 #home
        try:
            startdraw(filename)
        except IOError:
            print("Could not find or load file")
        