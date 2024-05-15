import turtle as t
import math
included_angle=int(input())
s=(180-(360-(included_angle*2))/2)/2;another_equal_angle=180-s
a=float(input())
sin=math.sin((math.pi)/180*s)
m=16*(a**4)*((sin**2))
another_length=(((4*(a**2)  - (math.sqrt((16*(a**4))-m))))/2)**(1/2)
print(another_length)
def triangle(length1,equal_length2,angle):
    length1=another_length
    equal_length2=a
    angle=included_angle
    if length1!=equal_length2:
        t.forward(length1)
        t.left(another_equal_angle)
        t.forward(equal_length2)
        t.left(angle)
        t.forward(equal_length2)
triangle(another_length,a,another_equal_angle)
t.done()