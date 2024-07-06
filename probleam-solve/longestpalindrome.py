# class Solution:
#     def longestPalindrome(self,s:str)->int:
#         ss = set([])
#         for letter in s:
#             if letter not in ss:
#                 ss.add(letter)
#             else:
#                 ss.remove(letter)
                
#         print(ss)
#         if len(ss) != 0:
#             return len(s)-len(ss)+1
#         else:
#             return len(s)
        
        
        
# s=Solution()
# print(s.longestPalindrome('abccccdd'))

# class Solution:
#     def sumOddLengthSubarrays(self, arr: list[int]) -> int:
#         list1=[]
#         if len(arr)>=3:
#             s=0
#             for i in range(len(arr)-2):
#                 list1.append(sum(arr[s:s+3]))
#                 s=s+1
                
#             list1.append(sum(arr))
#             list1.append(sum(arr))
#             return sum(list1)
#         else:
#             return sum(arr)
    
# s=Solution()
# print(s.sumOddLengthSubarrays( [1,4,2,5,3]))

class Solution:
    def specialArray(self, nums: list[int]) -> int:
        a = nums
        n = len(a)
        
        for x in range(n + 1):

            count = sum(1 for s in a if s >= x)
            
            if count == x:
                return x
        
        return -1



class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        l1 = []
        l2 = []
        m = len(s)//2
        v = ['a','e','i','o','u','A','E','I','O','U']
        
        for i in range(m):
            for j in v:
                if s[i]==j:
                    l1.append(s[i])
        for e in range(m,len(s)):
            for j in v:
                if s[e]==j:              
                    l2.append(s[e])
        return len(l1)==len(l2)
class Solution:
    def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        list1=[]
        atikur=nums1
        sin= nums2
        demon= nums3
        for i in sin:
            if i in atikur or i in demon:
                list1.append(i)
        for i in atikur:
            if i in sin or i in demon:
                list1.append(i)
        for i in demon:
            if i in sin or i in atikur:
                list1.append(i)
        f = list
        n = set
        return f(n(list1))
    