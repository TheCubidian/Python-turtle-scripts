from turtle import *
bk(25)
speed(0)
pencolor("purple")
pensize(5)
bgcolor("yellow")
fillcolor("lightgreen")
begin_fill()
for a in range(7):
    for b in range(6):
        for c in range(3):
            fd(50)
            lt(120)
        lt(60)
    end_fill()
    if a == 0:
        for d in range(2):
            lt(60)
            fd(50)
            begin_fill()
    if a == 1:
        for d in range(3):
            bk(50)
            if d == 0:
                rt(60)
            elif d == 1:
                lt(60)
            else:
                rt(60)
                bk(50)
            begin_fill()
    if a == 2:
        penup()
        rt(60)
        goto(-100, 43.30)
        pendown()
        begin_fill()
    if a == 3:
        penup()
        rt(60)
        goto(50, 43.30)
        pendown()
        begin_fill()
    if a == 4:
        penup()
        rt(60)
        goto(50, -43.30)
        pendown()
        begin_fill()
    if a == 5:
        penup()
        rt(60)
        goto(-100, -43.30)
        pendown()
        begin_fill()
end_fill()
mainloop()