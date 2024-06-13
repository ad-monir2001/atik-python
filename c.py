
# import turtle as t
# import random
# t.shape("turtle")
# t.speed(0)
# t.bgcolor("black") 
# a=0
# for x in range(350): 
#     a=a+1
#     # t.pencolor(colors[x%6]) 
#     t.pencolor('#%06x' % random.randint(0, 2**24 - 1))
#     t.width(a//180 + 1) 
#     t.forward(x) 
#     t.right(59)
# t.goto(0,0)
# t.write("Atikur",align="center",font=("",150,""))
# t.done()

# import turtle as t
# t.bgcolor("black")
# t.speed(0)
# t.color("cyan")
# angle = 0
# for _ in range(100):
#     t.forward(angle)
#     t.right(12)
#     angle = angle+1
# t.done()
# t.color('#%06x' % random.randint(0, 2**24 - 1))
# t.write("you create, and more.", align="center", font=("" ,20, ""))
import phonenumbers
from phonenumbers import timezone,geocoder,carrier
number=input('')
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone,'en')
sim_details=carrier.name_for_number(phone,'en')
register=geocoder.description_for_number(phone,'en')
print(number)
print(phone)
print(time)
print(sim_details)
print(register)