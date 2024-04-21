#!FUNCTION 
#*FUNCTION IS A BLOCK OF CODE WHICH ONLY RUNS WHEN IT IS CALLED.
#!RULES OF FUNCTION
#*def function_name(parameters):
#*   print("what will i do?")
#*   return [what will i return]
#*function_name()
# def add(**a):
#     for key,value in a.items():
#         print(key,value)
#         print (f"{key} is {value}")#*or i can use ("{} is {}"".format(key,value))
# add(Name=input("Name"),age=int(input("age")),clas=int(input("class")),division=input("division"))
def stud(name,**marks):
    print(name)
    for i,e in marks.items():
        print(i,e) 
    for a,s in zip(marks.keys(),marks.values()):
        print(a,s)
stud("Atikur",English1st=74,English2st=71,Physics=93)