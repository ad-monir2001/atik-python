
# #!traversing 
# for i in range(len(a)):                    #**for i in list:==for i in range(len(a)):**
#     print(a[i])        #**print(list[i])**
# for i in range(-1,-len(a)-1,-1) :              #**traversing with negative index**
    # print(a[i])
# #     print(a[i])#**write it(range(-start,-end,-step)) to run NT **range(-1,-len(a)-1,-1)=range(len(a)-1,-1,-1)***
# # s=[[12,15],[2,9],[3],[5],['Atik','Milon'=="Milon",6],[-1,5]]
# # print(s[4])
# #!list slicing
# a=[1,2,3,4,5,6,"A","S"]
# print(a[::])#**It(list[s:e:s]) is use for slicing** 
# #*print(list[start,e,step])=print(a.traverse)
# print(a[1::2])
# print(a[-1:-8:-2])
# print(len(a[-1]))
# s=[2,3,4,5,6]
# d=a+s#**list plus**
# print(d)
# f="Atik  Milon"
# print(list)(f)                                 #**It
# x.reverse()#**list.reverse()=print(a[-1:len:-1])**
# print(x)'''
# # x=[1,2,36,45,662,2,6365]
# # (x.sort(reverse=True))#**ascending=1,2,3,4 and descending=4,3,2,1**
# # print(x)#**list.sort()=ascending** **list.sort()=descending**
#  #!List comprehension#[i for i in list,condition]
# '''a=input().split()
# print(len(a))
# print(a)
# s=list(map(int,input().split()))#!list(map("int,float",input().split())) **it(list) is very important.
# print(s)
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
# '''ma=[[1,2,4,8],[5,2,3,5]]
# a=[]#Transpose 
# for row in range(4):#!        imp
#     b=[]            #!        or
#     for col in ma:  #!        ta
#         b.append(col[row])#!  nt.....
#     a.append(b)
# print(a)
#  #!result=[[inner loop]outer loop]
# a=[[col[row]for col in ma]for row in range(4)]
# print(a)'''
# '''a=[1,2,3,4,5,7,6,8,8,9,9]
# s=[]
# r=0
# for i  in a:
#     if i not in s:
#         r=r+1
#         s.append(i)
# print(r)
# k=2
# f=[]
# for i in a:
#     fq=a.count(i)
#     if fq==2 and i not in f:
#         f.append(i)
# print(f)
# j=[[j for j in range(5)if j != i]for i in range(5)]
# print(j)'''
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
# # T=int(input())
# # for u in range(T):
# #     def is_prime(n):
# #         if n <= 1:
# #             return False
# #         if n <= 3:
# #             return True
# #         if n % 2 == 0 or n % 3 == 0:
# #             return False
# #         i = 5
# #         while i * i <= n:
# #             if n % i == 0 or n % (i + 2) == 0:
# #                 return False
# #             i += 6
# #         return True

# #     def count_primes_up_to(limit):
# #         count = 0
# #         for num in range(2, limit + 1):
# #             if is_prime(num):
# #                 count += 1
# #         return count

# #     limit = int(input("Enter the limit: "))
# #     prime_count = count_primes_up_to(limit)
# #     print(f"The number of prime numbers up to {limit} is: {prime_count}")
# '''def N():#!If I want to call function.I will write def any name():.
#     print("Hello, Atikur Rahman")
# N()
# def sum(a,s):#parameters #*def sum(a=5,s=6):
#     print("The summation of a and s=",a+s)#!print(f"sum of {a} and{s}={a+s}")
#     print("Atikur Rahman and"," milon are friends")
# a=int(input())
# s=int(input())
# sum(a,s)#name(5,6)={a,s=input()}
# def any(name,age):
#     print(f"Hello {name}.I am {age} years old")
# name=input()
# age=input()
# any("Atik",17)
# any(name,age)
# def atikur(s):
#     print(s,"Atikur RAhman")
#     d=print(s,list(map(str,input().split())))
# s=input()
# atikur(s)
# def sum(a,b):
#     print(a+b)
# a=int(input())
# b=int(input())
# sum(a,b)
# def sum_with_return(a,b):
#     return a+b
# r=sum_with_return(9,b)
# r=r+4
# print(r)'''
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
# od=["sunday","monday","tuesday","wednesday","thursday"]
# cd=["saturday","friday"]
# w=False
# print(type(w))
# while not w:
#     rain=input(" value : ")
#     day=input("The day : ")
#     if day in od and rain:
#         print(input(f"{day} school has opened and it's raining=={rain}. Do you go to school?Write here Your dessition : "))
#         continue
#     elif day in od and not rain:
#         print(input(f"{day} school has opened and it's raining=={rain}. will you go to school?Write here Your dessition : "))
#     elif day in cd and rain:
#         print(input(f"{day} school has closed and it's raining=={rain}. Do you go to school?Write here Your dessition : "))
#         break
#     else:
#         print(input("What will you do? : "))
