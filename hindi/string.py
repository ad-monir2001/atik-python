# name='Atikur Rahman'
# #string indexing [start:end:step]
# print(name[-13::])


# a=['name','Atikur',True,None,False,12,36.325,]
# s=0
# for i in range(len(a)):
#     s=s+1
#     a[i]=a[-s]
    
# print(a)


class Solution:
    def __init__(self,n:int)->None:
        
        print()
        print()
        for i in range(1,n+1):
            print(' '*(n-i),end='',)
            print('*'*(2*i-1),end='')
            print('  ')
         
s=Solution(10)

for i in range(3):
    print()
# for i in range(1,n+1):
#     if (i==1 or i==n):
#         print('*'*n)
#     else:
#         print('*',end="")
#         print(' '*(n-2),end='')
#         print('*',end='')
#     print()
        