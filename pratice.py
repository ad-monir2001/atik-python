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

def choose_a():
    player=input("enter your choose : ")
    com=input("enter com choose : ")
    choose= {"play":player,"c":com}
    return choose

choose=choose_a()
dict={"Name":"Atikur","roll":choose}
print(choose)