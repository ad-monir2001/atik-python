#  #!OBJECT ORIENTED PROGRAMMING
# #oBJECT IS A COLLECTION OF DATA AND DEF.
# #O=attribute + method # all objs are members of a class
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
#    Body of parent class            ******
#!class child class(parent class):   ******
#    Body of child class             ******
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
# class Man:
#     def __init__(self,Name,age):
#         self.Name=Name;self.Age=age
#     def intro(self):
#         print("My Name is Atikur")
# class Atikur(Man):
#     def intro(self):
#         print(A.Name ,"is a student")
# class Shakib(Man):
#     def intro(self):
#       print(S.Name,"is", S.Age ,"years old")
# A=Atikur("Atikur",17);S=Shakib("Shakib",18)



# class student:
#     def __init__(self,*name,**marks):
#         for i in name:
#             print(i)
#         for e in marks:pass
#         print(marks)
# a=student("Atikur","rashel","sahed",m=80,r=90,s=87)



class rectangle:
    def __init__(self,height,width):
        self.heigth=height
        self.width=width
    def set_height(self,height):
        self.set__height=height
    def set_width(self,width):
        self.set__width=width
    def mainres(self):
        return self.set_height==self.set_width
A=rectangle(input(),input())
S=rectangle(int(input()),int(input()))
print(A.mainres())
print(S.mainres())
# Barisal board বহুনির্বাচনি প্রশ্নোত্তর 2016