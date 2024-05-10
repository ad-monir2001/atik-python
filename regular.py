
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

from unittest import removeResult


def add(a,n):
    return a+n

