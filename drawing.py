from turtle import *

title("smile face")
bgcolor("yellow")
speed(3)
pensize(10)

#the outline of smile face
penup()
goto(0,-200)
pendown()
circle(200)

#left eye
color("black")
penup()
goto(-50,50)
pendown()
seth(90)
circle(50,180)

#right eye
color("black")
penup()
goto (120,100)
pendown()
goto (50,65)
goto (120,30)

#mouth
color("red")
penup()
goto(75,-75)
pendown()
seth(90)
circle(75,-180)

#write
color("blue")
penup()
goto(-180,250)
pendown
write("happy everyday",font=("Courier", 30, "bold"))

done()
