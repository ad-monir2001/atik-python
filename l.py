
# for i in range(-1,-len(a)-1,-1) :              #**traversing with negative index**
    # print(a[i])
# #     print(a[i])#**write it(range(-start,-end,-step)) to run NT **range(-1,-len(a)-1,-1)=range(len(a)-1,-1,-1)***

# a=[1,2,3,4,5,6,858,5,6]
# s=[i+10 for i in a]#!it use to add any number with every number.
# print(s)
# d="atikur rahman"
# f=[i for i in d]#![i for i in d]=print(list(d))
# print(f)
# a=[i for i in range(1,20)if i%3==0 if i%5==0]
# print(a)#![i for i in range()]=list(range())
# a=["odd"if o%2!=0 else "even" for o in range(0,10)]
# print(a)'''
#=================================================#
#=================================================#
# # # '''ma=[[1,2,4,8],[5,2,3,5]]
# # # a=[]#Transpose 
# # # for row in range(4):#!        imp
# # #     b=[]            #!        or
# # #     for col in ma:  #!        ta
# # #         b.append(col[row])#!  nt.....
# # #     a.append(b)
# # # print(a)
# # #  #!result=[[inner loop]outer loop]
# # # a=[[col[row]for col in ma]for row in range(4)]
# # # print(a)'''
# # # j=[[j for j in range(5)if j != i]for i in range(5)]
# # # print(j)'''
#=================================================#
#=================================================#
# # a=[]
# # for i in range(5):
# #     for s in range(5):
# #         if s!=i:
# #             a.append(s)
# # print(a,end=" ")
# '''for i in range(5):
#     for s in range(i+1):
#         print(chr(65+i),end=" ")#!(65+i)=ascii number
#     print()'''
# '''a=15423
# #Armstrong number
# a=153#!a=input()
# nl=len(str(a))#!nl=len(a)
# s=0
# for i in str(a):#!for i in a:
#     s=s+int(i)**nl#!s=s+int(i)**nl
# if (a)==s:#!if int(a)==s:
#     print("A")
# else:
#     print("N")'''
# # count = 0
# # for i in range(1, 1000):
# #     print(i, end='\t')
# #     count += 1
# #     if count == 5:
# #         print()
# #         count=0
# '''def N():#!If I want to call function.I will write def any name():.
#     print("Hello, Atikur Rahman")
# N()
# def sum(a,s):#parameters #*def sum(a=5,s=6):
#     print("The summation of a and s=",a+s)#!print(f"sum of {a} and{s}={a+s}")
#     print("Atikur Rahman and"," milon are friends")
# #library function
# #*import random or(datetime,math)
# #!anything=random.randint or(datetime.datetime.today(),math.sqrt,(number),pi)
# # *lambda function
# # a=lambda:print("Hello Atikur")#!variable=lambda:argument
    
# #!print(variable.lower()or upper()or title(1stw....)or capitalize(1stw)or isalpha(alphabet)or swapcase(negative)or casefold(it is more powerful))or count((anything))
# #*variable.upper()#it use to do capital letter
# #!variable.lower()=list.casefold()#it use to do small letter
#                 #more powerful
# #*variable.title()#it turn capital letter of 1st letter of word
# #!variable.isalpha()or isdigit()
# #*variable.capitalize()
# #!variable.swapcase(negative)
# #*variable.replace(what will I change,new letter,How many)
# #!list.join()#it use to join string**join()--->list to string
# #*variable.split()#it use to make list       split(),list()---->string to list
# s=input()
# if s==s[-1:-len(s)-1:-1]:
#     print("yes")
# else:
#     print("no")
# #!string reversing
# a=input('string')
# a=a.split(" ")
# r=" "
# for i in a:
#     r=r+i[::-1]+" "
# print(r)'''