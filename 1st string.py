
# #print("a\ts")"
print("""PS C:\\Users\\User\\OneDrive\\Desktop\\atik-python> & c:/Users/User/OneDrive/Desktop/atik-python/myenv/Scripts/python.exe "c://Users//User//OneDrive//Desktop/atik-python//1st string.py\n""")#it print new line

##!DICTIONARY 
# #It(d[0]) use to call any element in dictionary
# #It(dictionary["v"]=element) use to add any dic,element in dictionary

DIC={"NAME":"ATIKUR RAHMAN","YEARS":17,"COUNTRY":"BANGLADESH"}
DIC["DICr"]={"A":"ATIKUR","S":"RAHMAN"}#It(dic_name["what will I change"]) use to include anything in dictionary .

# print(DIC["DISTRICT"]);"==";print(DIC.get("DISTRICT"))
# DIC.items() #*dict to tuple
# del DIC["DICr"]
# for i in DIC:
#     print(i)
# from os import curdir
# from sqlite3 import Cursor
# # import turtle
# t=turtle.Turtle()
# t.hideturtle()
# t.color("green")
# t.begin_fill()
# t.penup()
# t.goto(0,50)
# t.pendown()
# for i in range(6):
#   t.forward(100)
#   t.right(60)
# t.end_fill()

# import math

# t.goto(50,-(math.sqrt(6400)))
# t.color("red")
# t.begin_fill()
# t.circle(50)
# t.end_fill()

# t.penup()
# t.goto(0,50)
# t.forward(200)
# t.pendown()
# t.color("green")
# t.begin_fill()
# for i in range(6):
#   t.forward(100)
#   t.right(60)
# t.end_fill()
# t.goto(250,-(math.sqrt(6400)))
# t.color("red")
# t.begin_fill()
# t.circle(50)
# t.end_fill()
# turtle.exitonclick()
# import turtle
# import random
# t=turtle.Turtle()

# t.penup()
# t.goto(-100,50)
# '#ff0000'
# # t.speed(20)
# t.color('#%0x' % random.randint(0, 2**24 - 1))
# t.begin_fill()
# t.circle(50)
# t.end_fill()
# t.color('green')
# t.shape("turtle")
# t.speed(2)
# t.goto(-100,-150)
# t.shape("turtle")
# t.speed(2)
# t.forward(280)
# t.left(90)
# t.forward(250)

# t.forward(150)
# t.speed()
# t.goto(180,-190)
# t.speed(2)
# t.left(90)
# t.forward(90)
# t.goto(90,150)
# t.color('#%0x' % random.randint(0, 2**24 - 1))
# t.begin_fill()
# t.circle(50)
# t.end_fill()
# t.goto(-10,25)
# t.color("red")
import turtle
import random
t=turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()
t.goto(-100,-150)
a=0
t.pendown()
for i in range(20):
  a=a+7
  t.penup()
  t.goto(-100+a/4,(-150+a))
  t.pendown()
  t.pencolor("red")
  t.width(2)
  t.begin_fill()
#   t.color('#%06x' % random.randint(0, 2**24 - 1))
  t.circle(50)
  t.color("green")
  t.end_fill()
t.penup()
t.goto(100,-140)
t.pendown()
s=5
for e in range(30):
  s=s+3.5
  t.pencolor(('#%06x' % random.randint(0, 2**24 - 1)))
  t.width(2)
  t.circle(s)
t.penup()
t.goto(260,-160)
t.pendown()
t.pencolor("orange")
t.width(6)
for f in range(2):
    t.left(90)
    t.forward(350)
    t.left(90)
    t.forward(450)
t.penup()
t.goto(10,135)
t.pendown()
t.pencolor("Green")
t.width(6)
t.write("Atikur's  drawing.",align="center",  font=("" ,30, ""))
t.penup()
t.goto(23,110)
t.pendown()
t.color("red")
t.write("Here, two infinite circles have been drawn by Atikur Rahman.",align="center",font=("",11,""))
turtle.done()
