# a="123"
# s="456"
# print(eval(a)*eval(s))

# class Solution:
#     def ONePlus(self,digits:list)->list:

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(n):
            if 2**i==n:
                return True
            else:
                return False
my=Solution()
print(my.isPowerOfTwo(int(input())))
print(int(input())&int(input()))