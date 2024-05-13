import turtle as t
import math
a=int(input("Enter the equal sight of triangle : "))
angle=int(input("the included angle of triangle : "))
another_angle=180-((180-angle)/2)
b=[((a*2)**2 - math.sqrt((2*a)**4 -(4*(a**2)*math.sin(angle))**2))/2 ,((a*2)**2 + math.sqrt((2*a)**4 -(4*(a**2)*math.sin(angle))**2))/2]
for i in b:
    if i>0:
        another_side=i
        def triangle(length1,length2):
            length1=a
            length2=another_side
            t.forward(length2)
            t.left(another_angle)
            t.forward(length1)
            t.left(angle)
            t.forward(length1)
        triangle(a,another_side)
t.done()       