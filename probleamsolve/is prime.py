# class Solution:# bograha263964
#     def countPrimes(self, n: int) -> int:
#         res = 0
#         if n <= 2:
#             return 0
#         is_prime = [True] * n
#         is_prime[0] = is_prime[1] = False
#         for i in range(2,n):
#             if is_prime[i]:
#                 for j in range(i**2,n,i):
#                     is_prime[j] = False
#         return sum(is_prime)
    
    
# s=Solution()


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        listt=[]
        lists=[]
        list3=[]
        for i in t:
            listt.append(i)
        for e in s:
            if e in listt:
                list3.append('True')
                
            else:
                list3.append('False')
        return ''.join(list3)==True*len(s)  

            
            
s=Solution()
print(s.isSubsequence('abc','ahbgdc'))



