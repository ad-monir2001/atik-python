class Student:
    def __init__(self,Name:str,Roll:int) -> None:
        self.a=Name
        self.r=Roll
        print(f"{self.a}'s roll {self.r}")
        
a1=Student(input("Name : "),int(input("roll : ")))
a2=Student(input("Name : "),int(input("roll : ")))
print(a1.r)