from turtle import *

print('''This is a linear graph creator. This means the graph has a formula of y = mx + c
(m being gradient and c being y-intercept). This program works for y = mx graphs too.''')
gradient = float(input("What is the gradient? "))
y_intercept = input("What is the y-intercept? (leave blank if you are creating a y = mx graph) ")

speed(6)

if y_intercept == "":
    y_intercept = 0
else:
    y_intercept = float(y_intercept)
y = gradient * 300

hideturtle()
goto(-1200, 0)
fd(2400)
home()
goto(0, -600)
lt(90)
fd(1200)
if y_intercept == 0:
    home()
    pencolor("lightgreen")
    goto(1200, y)
    goto(-1200, -y)
else:
    goto(0, int(y_intercept))
    pencolor("tomato")
    goto(1200, y + y_intercept)
    goto(-1200, -y + y_intercept)
mainloop()