import turtle as t
import math
t.hideturtle()
a=float(input("equal_length : "))
included_angle=int(input("included angle : "))
counted_angle=180-included_angle
another_angle=180-(180-counted_angle)/2
pi=math.pi
another_length=(a*(math.sin((pi/180)*counted_angle)))/math.cos((pi/180)*(counted_angle/2)) ## a*sin(counted_angle)/cos(counted_angle/2)
print(another_angle)
t.pencolor(input("border color : "))
def triangle(L1,equal):
    if included_angle!=another_angle:  
        t.fd(L1)
        t.left(another_angle)
        t.fd(equal)
        t.left(included_angle)
        t.fd(equal)
        t.left(another_angle)
    else:
        print("L does not equal L2")
triangle(another_length,a)
t.done()
