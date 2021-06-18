#import libraries
import tkinter as tk
from tkinter import *
import turtle

class Sketch(tk.Tk):
    def __init__(self):
        global xCoord
        global yCoord
        xCoord = 0
        yCoord = 0

        super().__init__()
        self.title('Sketch')
        self.geometry('700x600')
        
        self.canvas = tk.Canvas()
        self.canvas.config(width=500,height=500)
        self.canvas.pack(side=tk.LEFT)
        self.screen = turtle.TurtleScreen(self.canvas)

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

        self.instructions = Text(width=12,height=20)
        self.instructions.place(x=510,y=280)

        self.pen = turtle.RawTurtle(self.screen)
        self.pen.reset()
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(-240,-240)
        self.pen.pendown()
        self.pen.showturtle()
        xCoord = 0
        yCoord = 0


    def moveUp(self):
        #print(self.pen.ycor())
        global yCoord
        self.pen.setheading(90)
        self.pen.forward(10)
        if(self.pen.ycor()>240):
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

    def penOn(self):

        self.pen.pendown()
        self.instructions.insert(INSERT,"Z0")
        self.instructions.insert(END,"\n")

    def penOff(self):
        self.pen.penup()
        self.instructions.insert(INSERT,"Z10")
        self.instructions.insert(END,"\n")
    
    def fileWrite(self):
        file = self.instructions.get('1.0', END)
        f = open("file.txt", "w+")
        f.write(file)
        f.close()

    
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

    
if __name__ == "__main__":
    window = Sketch()
    window.mainloop()