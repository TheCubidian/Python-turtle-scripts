from turtle import *
progression = 0
fillcolor("purple")
for a in range(4):
    begin_fill()
    for b in range(4):
        pendown()
        fd(100)
        rt(90)
    penup()
    end_fill()
    if progression == 1:
        goto(0, 100)
    elif progression == 2:
        goto(-100, 100)
    else:
        goto(-100, 0)
    progression += 1    
mainloop()