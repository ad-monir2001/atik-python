# class Solution:
#     def hasGroupsSizeX(self, deck: list[int]) -> bool:
#         l = list(set(deck))
#         final = []
#         for i in range(len(l)):
#             final.append(deck.count(l[i]))
#         for j in final:
#             if j%2 != 0:
#                 return False
#             else:
#                 return True



class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        l= [i**2 for i in nums].sort()
        return l
    
    
s=[-1,-9,5,-4]
p=([i for i in s])
p.sort()
print(p)