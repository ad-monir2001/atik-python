# class Solution:
    
#     def isPowerOfThree(self, n):
#         import math
#         if n<=0:
#             return False

#         res = round(math.log(n,3))
#         return 3**res==n
    



class Solution:
    def isPowerOfThree(self, n):
        if n<=0:
            return False
        while n%3==0:
            n=n//3
        return n==1
    
    
    
import math
print(math.log(9,3))