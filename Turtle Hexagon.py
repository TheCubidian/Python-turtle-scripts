from turtle import *
fillcolor("yellow")
bgcolor("lightgreen")
pensize(5)
speed(10)
penup()
goto(25, 0)
pendown()
begin_fill()
lt(120)
for a in range(3):
    begin_fill()
    for b in range(6):
        fd(50)
        lt(60)
    lt(120)
    end_fill()
mainloop()