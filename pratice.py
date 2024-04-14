# a=['😱','🙂','🥳','😭','🍎', '🍊', '🍎', '🍎', '🍊']
# import random
# s=a[random.randint(0,8)]
# p=a[random.randint(0,8)]
# if s==p:
#     print("There is nothing any player")
# else:
#     print(s,"VS",p)

# class Solution:
#     def checkPerfectNumber(self, num: int)->bool :
#         s=0
#         for e in range(1,num):
#                 for i in range(1,num):
#                     if num%e==0:
#                         if e==num:
#                             break
#                         a=e
#                         res=s+a
#                         s=res
#         return res == num    
# m=Solution()
# for f in range(1,10**8):
#     w=f
#     print(m.checkPerfectNumber(f))

    # Google. ...
    # University of Michigan. ...
    # Coursera Project Network. ...
    # University of Michigan. Python 3 Programming. ...
    # Google. Google IT Automation with Python. ...
    # Meta. Programming in Python. ...
    # University of Pennsylvania. Introduction to Programming with Python and Java. ...
    # Rice University. Python Programming Essentials.
from tkinter import NO


name=input("name : ")
handle=open(name,'r')
counts=dict()
for i in handle:
    word=i.split()
    for w in word:
        cuunts[word]=counts.get(w,0)+1
bigcount=None
bigword=None
for w,count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount=w
        bigcount=count
print(bigword,bigcount)