# t.color('#%06x' % random.randint(0, 2**24 - 1))
# t.write("you create, and more.", align="center", font=("" ,20, ""))
import random
import turtle as t
import colorsys as c
t.setup(800,800)
t.tracer(10)
t.width(2)
t.bgcolor("Black")
co=["black",'yellow','red','green','blue',"cyan","olive",'teal']


for _ in range(25):
    for i in range(15):
        for c in co:
        # t.color('#%06x' % random.randint(0, 2**24 - 1))
            t.color(c)
            t.color()
            t.right(90)
            t.circle(200-_*4,90)
            t.left(90)
            t.circle(200-_*4,90)
            t.right(180)
            t.circle(50,24)
t.hideturtle()
t.done()