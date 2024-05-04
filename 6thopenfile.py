class Man:
    def __init__ (self, intro:str):
        self.intro=intro
    def ans(self):
        return self.intro
class person:
    def __init__(self,Name,age,roll,intro):
        self.Name=Name;self.age=age;self.roll=roll
        self.p_intro=Man(intro)
    def ans2(self):
        return self.p_intro.ans()

a=person("Atikur",14,1,"Mandal")
print(a.ans2())
# class salary:
#     def __init__(self,pay,bonus):
#         self.pay=pay
#         self.bonus=bonus
#     def total_salary(self):
#         return self.pay*12 +self. bonus
# class Employee:
#     def __init__(self,Name,age,pay,bonus):
#         self.Name=Name
#         self.age=age
#         self.Emp_salary=salary(pay,bonus)
#     def total_salary2(self):
#         return self.Emp_salary.total_salary()
# e=Employee("Atikur",17,38000,12)
# print(e.total_salary2())