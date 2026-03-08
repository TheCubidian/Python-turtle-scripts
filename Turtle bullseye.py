from turtle import *
colours = []
ask = ("first", "second", "third", "fourth")
for a in range(4):
    colours.append(input("What colour do you want " + ask[a] + "? ").lower())
progression = 0
radius = 40
x_y = -25, -40
colour = colours[0]
for b in range (4):
    if progression == 1:
        colour = colours[1]
        radius = 35
        x_y = -25, -35
    elif progression == 2:
        colour = colours[2]
        radius = 20
        x_y = -25, -20
    elif progression == 3:
        colour = colours[3]
        radius = 10
        x_y = -25, -10
    penup()
    fillcolor(colour)
    begin_fill()
    goto(x_y)
    pendown()
    circle(radius)
    end_fill()
    progression += 1
mainloop()