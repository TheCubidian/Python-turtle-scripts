import math
from turtle import *
degrees, x, t, nums = 0, -905, Turtle(), (1, 2)
t.screen._root.state("zoomed")
t.hideturtle()
t.color("MediumBlue")
def choice():
    global graph
    graph = input("Do you want to draw a graph of sine or cosine? 1/2 ")
t.speed(0)
t.penup()
t.goto(-900,450)
t.pendown()
t.right(90)
t.fd(900)
t.goto(-900, 0)
t.left(90)
t.fd(1800)
t.bk(1800)
t.color("black")
choice()
while True:
    try:
        graph = int(graph)
        if graph in nums:
            break
        else:
            raise ValueError
    except ValueError:
        print("Your input was invalid. Try again. ")
        choice()
if graph == 1:
    for a in range(361):
        t.goto((x + 5), math.sin(math.radians(degrees)) * 450)
        degrees += 1
        x += 5
else:
    t.goto(-900, 450)
    for a in range(361):
        t.goto((x + 5), math.cos(math.radians(degrees)) * 450)
        degrees += 1
        x += 5
mainloop()