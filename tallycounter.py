# A simple tally counter using turtle module
# by - zaid-hassan 
# Date: 21-Dec-22 Time: 11:52 PM

import turtle

w = turtle.Screen()
w.title("Tally-counter by zaid-hassan")
w.bgcolor("black")
w.setup(width=600, height=600)
w.tracer(0)

# counter
c = turtle.Turtle()
c.speed(0)
c.color("green")
c.penup()
c.hideturtle()
c.goto(0, -30)
c.write("0", align="center", font=("digital-7", 100, "bold"))

# instructions
instr = turtle.Turtle()
instr.speed(0)
instr.color("green")
instr.penup()
instr.hideturtle()
instr.goto(0, 190)
instr.write("Press C to count | R to reset | Esc to exit", align="center", font=("digital-7 italic", 15, "bold"))

# counter program
count = 0
def counter():
    global count
    count += 1
    c.clear
    c.write("{}".format(count), align="center", font=("digital-7", 100, "bold"))

def reset():
    global count
    count = 0
    c.clear()
    c.write("{}".format(count), align="center", font=("digital-7", 100, "bold"))

def exit():
    turtle.Screen().bye()

# Key
w.listen()
w.onkeypress(counter, "c") or w.onkeypress(counter, "C")
w.onkeypress(reset, "r") or w.onkeypress(counter, "R")
w.onkeypress(exit, "Escape")

turtle.done()