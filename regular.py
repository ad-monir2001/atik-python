# from typing import Counter
# class Solution:
#     def majorityElement(self, nums):
#         return Counter(nums).most_common()[0][0]  
# m=Solution()
# print(m.majorityElement(list(input().split())))     
# class Solution:
#     def longestCommonPrefix(self, v: List[str]) -> str:
#         ans=""
#         v=sorted(v)
#         first=v[0]
#         last=v[-1]
#         for i in range(min(len(first),len(last))):
#             if(first[i]!=last[i]):
#                 return ans
#             ans+=first[i]
#         return ans 
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         strs.sort()
#         pre = []
        
#         for a,b in zip(strs[0], strs[-1]):
#             if a == b:
#                 pre.append(a)
#             else:
#                 break
        
#         return "".join(pre)
a=["Atikur","Hohey","Mitchel","Atridoy"]
s=[]
for i , e in (a[0],a[-1]):
    if i==e:
        s.append(a)
    else:
        break
    print("".join(s))