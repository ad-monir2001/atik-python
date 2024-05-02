#  #!OBJECT ORIENTED PROGRAMMING
# #oBJECT IS A COLLECTION OF DATA AND DEF.
# #O=attribute + method # all objs are members of a class
class Main:
    def A(self,wide,height):
        self._wide=wide
        self._height=height
class Colouring:
    def colour(self,color):
        self._color=color
    def rint(self):
        return self._color
#####CLASS OF RECTANGLE
class rectangle(Main,Colouring):
    def area(self):
        res= self._height*self._wide
        return res
####CLASS OF TRIANGLE
class triangle(Main,Colouring):
    def area(self):
        res= self._height*self._wide/2
        return res

#####TRIANGLE RESULT
trian=triangle()
trian.A(20,15)
trian.colour("Red")
print(trian.area())
print(trian.rint())

####RECTANGLE RESULT
rectan=rectangle()
rectan.A(60,2)
rectan.colour("Green")
print(rectan.area())
print(rectan.rint())
