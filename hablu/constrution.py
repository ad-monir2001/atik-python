
class ClassMethod:
    def instancemethod(self):
        print("This is an instance method")
    @classmethod
    def classmetho(L):
        print("This is a class method")

    @staticmethod
    def Staticmethod():
        print("This is a staticmethod")
v=ClassMethod()
v.instancemethod()
v.classmetho()
v.Staticmethod()
ClassMethod.classmetho()
ClassMethod.Staticmethod()
