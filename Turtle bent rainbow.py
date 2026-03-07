from turtle import *
colours = ("red", "orange", "yellow", "lightgreen", "dodgerblue", "indigo", "violet")
radius = (100, 85, 70, 60, 45, 30, 15)
penup()
goto(0, -100)
for a in range (7):
    fillcolor(colours[a])
    begin_fill()
    circle(radius[a])
    end_fill()
mainloop()