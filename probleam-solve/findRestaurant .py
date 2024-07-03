# from numpy import greater


# class Solution:
#     def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
#         set1=set(list1)
#         set2=set(list2)
        
#         res=list(set1.intersection(set2))
#         for i in res:
#             if len(i)>8:
#                     res=list(set1.intersection(set2))
        
# s=Solution()
# print(s.findRestaurant( ["Shogun","Tapioca Express","Burger King","KFC"], ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"],))
# class Solution:
#     def isValid(self, s:str) ->bool:
#         if '()' in s or '[]' in s or "{}" in s:
#             res=s.replace("()",'').replace("[]",'').replace("{}",'')
#         return len(res)==0
# s=Solution()
# print(s.isValid("()[]{}"))

# class Solution:
#     def subsets(self, nums: list[int]) -> list[list[int]]:
#         subsets = [[]]
#         for elem in nums:
#             subsets=subsets+ [subset+[elem] for subset in subsets]
#         return subsets
# s=Solution()
# print(s.subsets([1,2,3]))
# print([1,2]+[1])
# class Solution:
#     def wordBreak(self, s: str, wordDict: list[str]) -> bool:
#         join1=''.join(wordDict)
#         if len(s)>len(join1):
#             return s.startswith(join1) or s.endswith(join1)
#         if len(s)<len(join1):
#             return join1.startswith(s) or join1.endswith(s)
#         if len(s)==len(join1):
#             return s.startswith(join1)
# s=Solution()
# print(s.wordBreak("leetcode",["leet","code"]))

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        s=-1
        for i in numbers:
            s=s+1
            if target==numbers[s]+numbers[-s]:
                return [numbers.index(numbers[s]),numbers.index(numbers[-s])]


s=Solution()
print(s.twoSum( [2,7,11,15],9))

# Python Tutorial For Beginners in Hindi | Complete Python Course 🔥