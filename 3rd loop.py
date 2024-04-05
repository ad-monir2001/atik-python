# class Solution:
#     def complexNumberMultiply(self, num1: str, num2: str) -> str:
#         self.a=num1
#         self.s=num2
#         res = eval(num1)*eval(num2)
#         return res
# m=Solution()
# print(m.complexNumberMultiply((input()),input()))
# class Solution:
#     def sumOfMultiples(self, n: int):
#         c=0
#         for i in range(1,n,3):
#             c=c+1
#             res = int (c + i)
#             return int(res)
# my=Solution()
# print(my.sumOfMultiples(int(input())))
p=0
r=int(input())
for i in range(3,r+1,3): 
    n= p+ i
    p=n
    print(i) 