#  #!OBJECT ORIENTED PROGRAMMING
# #*oBJECT IS A COLLECTION OF DATA AND DEF.
# #O=attribute + method #* all objs are members of a class
# class rules:
# #!class Class Name():
# #!   def __init__(self ,attribute1,attribute2):#pare
# #*      self .attribute1=attribute1
# #*      self .attribute2=attribute2
# #!   def methodname(self):
# #*      statement(s)
#     print()
# #* obj name=className(parameters)####obj
# class object_oriented():
#     def __init__(self,first_Name , money):
#         self.Name=first_Name
#         self.mo=money+int(input("last_added_money : "))

#     def full_function(self,last_Name,last_added_money):
#         self.mo=self.mo+last_added_money
#         self.Name=self.Name+last_Name
#         print(f"{last_added_money} is my total amount")
# # introduction=introduction.full_function()
# introduction=object_oriented(first_Name=input("Name : "),money=eval(input('amount : ')))
# print((introduction.mo))
#!ONE
# class Car:
#     def __init__(self,Name:str,Creator:str,Color:str,Making_Year):
#         self.name=Name
#         self.color=Color
#         self.Making_y=Making_Year
#         self.Creator=Creator
#     import datetime
#     def The_methods_of_this_Car_are(self):

#         assert self.Making_y!=datetime.date.today(); "It is possible to make any car in today.so it is wrong ."
        
#         print(self.name)
#         print(self.color)
#         print(self.Creator)
#         print(self.Making_y)

#         print("start the engine")
#         print("Press the break")
#         print("please drive")
#         print("turn left and right")
#         print("Change gear")

# import datetime
# Shakib=Car(input("shakib's Car Name : "),input("shakib's Car creator : "),input("shakib's Car Color : "),(datetime.datetime.today()))
# print(Shakib.The_methods_of_this_Car_are())

# Atikur=Car(input(f"Atikur's Car Name : "),input(f"Atikur's Car creator : "),input(f"Atikur's Car Color : "),(datetime.datetime.today()))
# print(Atikur.The_methods_of_this_Car_are())

# import calendar
# Milon=Car(input("Milon's Car Name : "),input("Milon's Car creator : "),input("Milon's Car Color : "),(calendar.TextCalendar(firstweekday=6).formatyear(int(input("Calender : ")))))
# (Milon.The_methods_of_this_Car_are())

# INHERITANCE                        ******
#!class parent class():              ******
#*   Body of parent class            ******
#!class child class(parent class):   ******
#*   Body of child class             ******
# class Man:
#     """Base class for all Man"""
#     def __init__(self,Name,age:int,company):
#         self.Name=Name
#         self.age=age    
#         self.company=company
#     def re(self):
#         print(f"{self.Name} is work at {self.company} company")
# person1=Man("a",1,"hacker")
# person1.company=(input("company : "))
# person1.re()
# class student(Man):
#     def __init__(self,Name,age,company):
#         Man.__init__(self,Name,age,company)
# student1=Man("ft",10,"Apple") 
# student1.company=person1.company
# (student1.re())
#!POLYMORPHISM
#!
class Man:
    def __init__(self,Name,age):
        self.Name=Name;self.Age=age
    def intro(self):
        print("My Name is Atikur")
class Atikur(Man):
    def intro(self):
        print(A.Name ,"is a student")
class Shakib(Man):
    def intro(self):
      print(S.Name,"is", S.Age ,"years old")
class Milon(Man):
    def intro(self):
        print(f"{self.Name} is my friend")
A=Atikur("Atikur",17);S=Shakib("Shakib",18)
M=Milon("Milon",17)
for N in [A,S,M]:
    (N.intro())

    