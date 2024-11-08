import turtle

#set screen and pen
screen = turtle.Screen()
screen.title("smile face")
screen.bgcolor("yellow")
pen = turtle.Turtle()
pen.speed(10)
pen.pensize(10)

#the outline of smile face
pen.penup()
pen.goto(0,-200)
pen.pendown()
pen.circle(200)

#left eye
pen.color("black")
pen.penup()
pen.goto(-50,50)
pen.pendown()
pen.setheading(90)
pen.circle(50,180)

#right eye
pen.color("black")
pen.penup()
pen.goto (120,100)
pen.pendown()
pen.goto (50,65)
pen.goto (120,30)

#mouth
pen.color("red")
pen.penup()
pen.goto(75,-75)
pen.pendown()
pen.setheading(90)
pen.circle(75,-180)

#write
pen.color("blue")
pen.penup()
pen.goto(-180,250)
pen.pendown
pen.write("happy everyday",font=("Courier", 30, "bold"))

pen.hideturtle()
screen.exitonclick


