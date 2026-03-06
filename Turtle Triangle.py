from turtle import *
fillcolor("red")
penup()
goto(0, -100)
pendown()
begin_fill()
bk(150)
for a in range(3):
    fd(300)
    lt(120)
end_fill()
mainloop()