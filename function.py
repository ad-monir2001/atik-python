# import turtle as t
# import math
# t.hideturtle()
# a=float(input("equal_length : "))
# included_angle=int(input("included angle : "))
# counted_angle=180-included_angle
# another_angle=180-(180-counted_angle)/2
# pi=math.pi
# another_length=(a*(math.sin((pi/180)*counted_angle)))/math.cos((pi/180)*(counted_angle/2)) ## a*sin(counted_angle)/cos(counted_angle/2)
# print(another_angle)
# t.pencolor(input("border color : "))
# def triangle(L1,equal):
#     if included_angle!=another_angle:  
#         t.fd(L1)
#         t.left(another_angle)
#         t.fd(equal)
#         t.left(included_angle)
#         t.fd(equal)
#         t.left(another_angle)
#     else:
#         print("L does not equal L2")
# triangle(another_length,a)
# t.done()
# import turtle as t
# import math
# pi=math.pi

# #============================================
# #                                           |
#         #         A                         |
#         #        /\        θ = /_B=/_C      |
#         #       /  \       /_A=180-θ        |
#         #      /    \                       |
#         #    a/      \ a                    |
#         #    /        \                     |
#         #   /          \                    |
#         #  /____________\                   |
#         # B      b      C                   |
# #                                           |
# # #==========================================
# #                                                                          
# a=int(input("equal_length : "))                                          
# θ=int(input("Take an equal angle to draw an Isosceles triangle : "))      
# included_angle=360-θ*2                                                 
# counted_angle=180-θ        
# b=2*a*math.cos(pi/180*(counted_angle))                                  
# color=["red","cyan","green","olive","Teal","orange"]                   

# # =============================================

# def equilateral_triangle(equal_length,another_length,theta):
#     for i in range(len(color)):
#         c=color[i]
#         if 2*counted_angle<180:
#           if counted_angle!=60:
#             t.begin_fill()  
#             t.color(c)
#             t.forward(another_length)
#             t.left(theta)
#             t.forward(equal_length)
#             t.left(included_angle)
#             t.forward(equal_length)
#             t.left(theta)
#             t.end_fill()
#           else:print("to draw a Isosceles triangle a!=b!=c ")
#         else:print("total angle of a triangle is 180")
# equilateral_triangle(a,b,θ)
# t.hideturtle()
# t.done()
