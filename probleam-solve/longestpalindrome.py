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

class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        list1=[]
        if len(arr)>=3:
            s=0
            for i in range(len(arr)-2):
                list1.append(sum(arr[s:s+3]))
                s=s+1
                
            list1.append(sum(arr))
            list1.append(sum(arr))
            return sum(list1)
        else:
            return sum(arr)
    
s=Solution()
print(s.sumOddLengthSubarrays( [1,4,2,5,3]))