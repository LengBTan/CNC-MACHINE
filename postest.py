
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
    f=open("drawtest.txt", "r")
    if f.mode =="r":
        contents = f.read()
        print(contents)
