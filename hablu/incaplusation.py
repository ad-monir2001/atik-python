from asyncio import Barrier

# Incaplusation

class Car:
    def __init__(self,Name,Color,code,):
        self.__Name=Name
        self.__Color=Color
        self.__code=code# I use __code to save code
    def print(self,):
        print("ATikur RAhman")


V1=Car("BMW","red","256@26Atikur")
print(V1.__code)