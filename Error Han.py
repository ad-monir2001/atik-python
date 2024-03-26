 #!ERRORHandling ARE {
    #*{TypeError,TimeoutError,TabError,AttributeError,ArithmeticError,AssertionError,BlockingIOError,ConnectionRefusedError,FileNotFoundError,IndexError,KeyError,MemoryError,NameError,SyntaxError,SystemError,ZeroDivisionError}


try :
    N=int(input())
    a=10/N
    print(a)
except ZeroDivisionError as m:
    print(m)
except ValueError as y:
    print(y)
try:
    pri
except NameError as n:
    print(n)
finally:
    print("")
