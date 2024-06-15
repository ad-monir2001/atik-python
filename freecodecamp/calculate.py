

x=float(input("x ; "))
y=float(input('y ; '))
z=round(x+y)
print(z)
print(f'{z:22,}') 

# (values:object,sep:str|None=" ",end:str|None="\n",file:SupportsWrite[str]|None=None,flush:Literal[False] =False)->None
# (values:object,sep:str|None=" ",end:str|None="\n", file:_SupportsWriteAndFlush[str]|None=None,flush:bool)->None
#Prints the values to a stream,or to sys.stdout by default.

a=x/y
print(f'{a:.9f}')# after int number it count 9 digit.