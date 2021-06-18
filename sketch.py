# import libraries
import tkinter as tk
from tkinter import *
import turtle

# Sketch class. Sets up the GUI and Turtle drawing interface.
# tk.Tk parameter is the tkinter gui library
class Sketch(tk.Tk):

    # Initialize variables, window, canvas, and buttons for the current instance of the class.
    # self parameter - current instance of the class.
    def __init__(self):

        # Stores X and Y coordinates, accessed by diffrent functions.
        global xCoord
        global yCoord
        xCoord = 0
        yCoord = 0

        super().__init__() #returns object as parent class
        self.title('Sketch')
        self.geometry('700x600')
        
        #setup canvas
        self.canvas = tk.Canvas()
        self.canvas.config(width=500,height=500)
        self.canvas.pack(side=tk.LEFT)
        self.screen = turtle.TurtleScreen(self.canvas) # place Turtle in tkinter as a widget. 

        #setup button size and placement on the window
        self.upButton = tk.Button(self, text="Up", command= self.moveUp, width=5, height=1, compound="c")
        self.upButton.place(x=550,y=0)
        self.leftButton = tk.Button(self, text="Left", command= self.moveLeft, width=5, height=1, compound="c")
        self.leftButton.place(x=500,y=20)
        self.rightButton = tk.Button(self, text="Right", command= self.moveRight, width=5, height=1, compound="c")
        self.rightButton.place(x=600,y=20)
        self.downButton = tk.Button(self, text="Down", command= self.moveDown, width=5, height=1, compound="c")
        self.downButton.place(x=550,y=40)

        self.penOff = tk.Button(self, text="Pen Up", command= self.penOff, width=8, height=2, compound="c")
        self.penOff.place(x=540,y=70)
        self.penOn = tk.Button(self, text="Pen Down", command= self.penOn, width=8, height=2, compound="c")
        self.penOn.place(x=540,y=110)
        
        self.fileWrite = tk.Button(self, text="Export", command= self.fileWrite, width=8, height=2, compound="c")
        self.fileWrite.place(x=540,y=150)

        self.penClear = tk.Button(self, text="CLEAR", command= self.penClear, width=8, height=2, compound="c")
        self.penClear.place(x=540,y=200)

        #setup text field size and position
        self.instructions = Text(width=12,height=20)
        self.instructions.place(x=510,y=280)

        #move pen to bottom left corner instead of middle of screen (origin)
        self.pen = turtle.RawTurtle(self.screen)
        self.pen.reset()
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(-240,-240)
        self.pen.pendown()
        self.pen.showturtle()
        xCoord = 0
        yCoord = 0

    # moveUp/Left/Right/Down direction button action.
    # Is called after a button is pressed from __init__

    def moveUp(self):
        #print(self.pen.ycor())
        global yCoord
        self.pen.setheading(90)
        self.pen.forward(10)
        if(self.pen.ycor()>240): # Checks if the coordinate of the Y position is more than 240. If it is, it undos the last pen movement, else it move the pen, adds 1 to the current Y coordinate, and inserts the current coordinate into the text field.
            self.pen.undo()
        else:
            yCoord += 1
            self.instructions.insert(INSERT,"Y")
            self.instructions.insert(INSERT,yCoord)
            self.instructions.insert(END,"\n")
            #print(yCoord)

    def moveLeft(self):
        global xCoord
        self.pen.setheading(180)
        self.pen.forward(10)
        if(self.pen.xcor()< (-240)):
            self.pen.undo()
        else:
            xCoord -=1
            self.instructions.insert(INSERT,"X")
            self.instructions.insert(INSERT,xCoord)
            self.instructions.insert(END,"\n")
            #print(xCoord)

    def moveRight(self):
        global xCoord
        self.pen.setheading(0)
        self.pen.forward(10)
        if(self.pen.xcor()>240):
            self.pen.undo()
        else:
            xCoord +=1
            self.instructions.insert(INSERT,"X")
            self.instructions.insert(INSERT,xCoord)
            self.instructions.insert(END,"\n")
            #print(xCoord)
    
    def moveDown(self):
        global yCoord
        self.pen.setheading(270)
        self.pen.forward(10)
        print(self.pen.ycor())
        if(self.pen.ycor()<-240):
            self.pen.undo()
        else:
            yCoord -= 1
            self.instructions.insert(INSERT,"Y")
            self.instructions.insert(INSERT,yCoord)
            self.instructions.insert(END,"\n")
            #print(yCoord)

    # pen On/Off button action. When pressed, pen is raised, or lowered, and inserts Z coordinates of the pen.
    def penOn(self):

        self.pen.pendown()
        self.instructions.insert(INSERT,"Z0")
        self.instructions.insert(END,"\n")

    def penOff(self):
        self.pen.penup()
        self.instructions.insert(INSERT,"Z10")
        self.instructions.insert(END,"\n")
    
    #fileWrite button action. When "export" button is pressed, creates a new file, and exports the coordinate text field into the new file.
    def fileWrite(self):
        file = self.instructions.get('1.0', END)
        f = open("file.txt", "w+")
        f.write(file)
        f.close()

    #When clear button is pressed, clears the canvas, and moves the pen cursor to the bottom left of the screen.
    def penClear(self):
        global xCoord
        global yCoord
        self.pen.reset()
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(-240,-240)
        self.pen.pendown()
        self.pen.showturtle()
        xCoord = 0
        yCoord = 0
        self.instructions.delete('1.0',END)

    #main, opens the GUI
if __name__ == "__main__":
    window = Sketch()
    window.mainloop()