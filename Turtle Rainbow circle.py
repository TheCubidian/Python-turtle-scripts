from turtle import *
speed(6)
colours = ("red", "orange", "yellow", "lightgreen", "dodgerblue", "indigo", "violet")
radius = (100, 85, 70, 60, 45, 30, 15)
for a in range (7):
    penup()
    goto(0, -radius[a])
    pendown()
    fillcolor(colours[a])
    begin_fill()
    circle(radius[a])
    end_fill()
mainloop()