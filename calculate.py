# import turtle as t
# import math
# t.penup()
# t.goto(-100,10)
# t.pendown()
# cone=int(input("included angle "))
# included_angle=180-cone
# another_equal_angle=180-(180-cone)/2
# print(another_equal_angle)
# a=float(input("equal length "))
# sin=math.sin((math.pi)/180*cone)
# m=16*(a**4)*((sin**2))
# anothercounted_length=(((4*(a**2)  - (math.sqrt((16*(a**4))-m))))/2)**(1/2)
# anothercounted_length2=(((4*(a**2)  + (math.sqrt((16*(a**4))-m))))/2)**(1/2)
# print(anothercounted_length2)
# def triangle(length1,equal_length2):
#     if cone>90:
#         length1=anothercounted_length2
#     else:
#         length1=anothercounted_length
#     equal_length2=a
    
#     if length1!=equal_length2:
#         c=input("pencolor : ")
#         t.pencolor(c)
#         t.forward(length1)
#         t.left(another_equal_angle)
#         t.forward(equal_length2)

#         t.left(included_angle)

#         t.forward(equal_length2)
#         t.left(another_equal_angle)
#     else:
#         print("to draw a triangle length!=equal length")
# if cone>90:
#     triangle(anothercounted_length2,a)
# else:
#     triangle(anothercounted_length,a)

# t.done()

import turtle as t
import math
a=float(input("equal_length : "))
included_angle=int(input("included angle : "))
counted_angle=180-included_angle
another_angle=180-(180-counted_angle)/2
pi=math.pi
another_length=(a*(math.sin((pi/180)*counted_angle)))/math.cos((pi/180)*(counted_angle/2))
print(another_angle)
t.pencolor(input("border color : "))
def triangle(L1,equal):
    L1=another_length
    equal=a
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