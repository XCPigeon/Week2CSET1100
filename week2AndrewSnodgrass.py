"""
For credit you must:

1) Make these instructions a comment at the beginning of your program

2) Use the turtle graphics commands, but not the write command.

3) Draw UT in block letters

4) Draw your initials in block letters

5) Comment your code indicating what each section is doing.

6) Submit your .py file to Blackboard.  DO NOT SUBMIT YOUR .sln FILE.  ONLY THE .py FILE.
"""
import turtle
import time

def tee():#this user defined function will make a t. I'm going to do this because there is a t in both my initals and ut
    #top box
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(45)#leaving room for the bottom box
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()
    turtle.forward(45)#bottom line done
    turtle.right(90)
    turtle.forward(10)
    turtle.backward(10)#lets go back to the bottom box
    turtle.right(90)
    turtle.forward(45)
    turtle.right(90)
    turtle.forward(140)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(140)
    
def getready(x):#this is to get the turtle in the same spot each time.
    while (int(x) != 0):
        turtle.left(90)
        turtle.forward(90)
        x -= 1
    else:
        turtle.left(90)
    
#before we do anything, lets get where we want to be
turtle.bgcolor("yellow")
turtle.pencolor("blue")
turtle.pensize(5)
turtle.penup()
getready(2)
turtle.pendown()
#lets make the u
turtle.forward(100)
turtle.circle(50,180)#(radius, degreeses)
turtle.forward(100)
turtle.left(90)
turtle.forward(10)#from this point forward, the u portions need to be 10 smaller
turtle.left(90)
turtle.forward(90)
turtle.circle(-40,180)
turtle.forward(90)
turtle.left(90)
turtle.forward(10)
#heading to the start of the "T"
turtle.penup()
turtle.right(180)
turtle.forward(110)
turtle.pendown()
#make a t
tee()
#getting readdy for my Initals
turtle.penup()
turtle.setpos(0,0)#to get back to the center
turtle.right(90)#to get to how we was
turtle.hideturtle()
time.sleep(5)#lets stop and admire the work...
turtle.showturtle()
##################################################okay times up
turtle.reset()
turtle.bgcolor("purple")
turtle.pencolor("green")
turtle.pensize(5)
turtle.penup()
getready(1)
turtle.forward(50)
#GIVE ME AN 'A'
turtle.pendown()
turtle.left(75)
turtle.forward(158)
turtle.left(105)
turtle.forward(10)
turtle.left(75)
turtle.forward(79)
turtle.right(75)
turtle.forward(20.9)
turtle.right(75)
turtle.forward(79)
turtle.left(75)
turtle.forward(10)
turtle.left(105)
turtle.forward(158)
turtle.right(105)
#get ready for a "T"
turtle.penup()
turtle.forward(60)
turtle.pendown()
#do a t
tee()
#tada
