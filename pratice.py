# import re
# a="phone:+8801784 040029,+6501321-544143,01235152,+9901721-794952,+8801829 -236514"
# p=(re.findall(r"01[35879]\d{2}\-*\s*\d{6}",a))
# print(p)

# import turtle as t
# for i in range(2):
#     t.begin_fill()
#     t.color("green","green")
#     t.forward(200)
#     t.right(90)
#     t.forward(120)
#     t.right(90)
#     t.end_fill()

# t.color("green")
# t.right(45)
# t.forward(110)
# t.begin_fill()
# t.color("red","red")
# t.circle(26.6190379)
# t.end_fill()
# t.exitonclick()
# a=int(input("please "))
# print(a)
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) :
#         self.s=s
#         self.a=[]
#     def count(self):

#         print(len(set(self.s)))


# my=Solution()
# my.s=input()
# a=[]
# for i in my.s:
#     if i not in a:
#         a.append(i)
# print(len(a))
# my.count()
# class Solution:
#     def reverse(self, x: int):
#         self.x=x
#     def
# a=int(input())
# s=str(a)
# l=[]
# for i in range(-1,-len(s)-1,-1):
#     l.append((s[i]))
# print("".join(l))
# a=input('string')
# a=a.split(" ")
# r=" "
# for i in a:
#     r=r+i[::-1]+" "
# print(r)
# for i in range(-1,-len(a)-1,-1) :
# a=int(input())
# rev=0
# while a>0:
#     last_d=a%10
#     rev=rev*10+last_d
#     a=a//10
# print(rev)


# a=23651
# s=str(a)
# l=list(s)
# if l[0]=="-":
#     l.append("-")
#     l.remove("-")
#     p=("".join((l[-1:-len(l)-1:-1])))
#     print(p)
# else:
#     f=("".join(s[-1:-len(s)-1:-1]))
# class Solution:
#     def reverse(self, x: int) :
#         self.x=int(x)
#     def re(self):
#         s=str(my.x)
#         l=list(s)
#         if l[0]=="-":
#             l.append("-")
#             l.remove("-")
#             print(int("".join((l[-1:-len(l)-1:-1]))))
#         else:
#             print(int("".join(s[-1:-len(s)-1:-1])))
# my=Solution()
# my.x=int(input())
# my.re()

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res=0
        if divisor > 0 : 
            res= 0
        if dividend == int:
            res=int(dividend//divisor)
        return res
# class Solution:
#     def reverse(self, x: int) -> int:
#         res = 0
#         if x < 0:
#             res = int(str(x)[1:][::-1]) * -1
#         else:
#             res =int(str(x)[::-1])
        
#         if res>2**31-1 or res<-2**31:
#             res = 0
        
#         return res
#     def myPow(self, x: float, n: int) -> float:
#         res = (x**n)
#         return res
# my=Solution()

# print(my.myPow(float(input()),int(input())))

# class Solution:
    
#     def myPow(self, x: float, n: int) -> float:
#         if n == 0:
#             return 1
#         elif n == 1:
#             return x
#         elif n == -1:
#             return 1/x
#         return self.myPow(x, n//2) * self.myPow(x, n//2) * self.myPow(x, n%2)