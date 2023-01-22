import turtle

myTurtle = turtle.Turtle() # initialization of the module
myWin = turtle.Screen() # initialization of the screen

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen) #move forward
        myTurtle.right(45) # move right with a 90 degree angle
        drawSpiral(myTurtle,lineLen-10) #draw the above movements

drawSpiral(myTurtle,200)
myWin.exitonclick()