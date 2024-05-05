import turtle 
t=turtle.Turtle()
t.hideturtle()
t.color("green")
t.begin_fill()
for i in range(2):
    
    t.forward(150)
    t.right(90)
    t.forward(100)
    t.right(90)

t.end_fill()
t.penup()
t.goto(100,-50)
t.pendown()
t.color("red")
t.begin_fill()
t.circle(20)

t.end_fill()
turtle.exitonclick()

# ! HOME work

# make a hexagonal (sorovuj)