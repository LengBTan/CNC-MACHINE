
from io import StringIO


pos1 = 64
pos2 = 1

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



move(xcoord, pos1)
print("current coord is:", xcoord)
move(xcoord, pos2)
print("current coord is:", xcoord)

if __name__ == "__main__":
    
    while True:
        filename = input("input")
        try:

            f = open(filename, "r")
            data = f.read()
            lines = data.splitlines()
            for i,line in enumerate(lines):
                #print(line)
                if "X" in line:
                    xNext = line[1:]
                    print(xNext)
                if "Y" in line:
                    yNext = line[1:]
                    print(yNext)
                if "Z" in line:
                    zNext = line[1:]
                    print(zNext )
            f.close
        except IOError:
            print("could not find/load file")