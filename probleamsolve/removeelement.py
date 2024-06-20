# class Solution:
#     def removeDuplicates(self, nums: list) -> int:
#         for i in nums:
#             if nums.count(i)>1:
#                 nums.remove(i)
#         return nums
    
    
# s=Solution()
# print(s.removeDuplicates([1,1,2]))

class Solution:
    def removeDuplicates(self, nums: list) -> int:
        set1=set(nums)
        return (set1)
    
s=Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
# list=[1,1,2]
# for i in list:
#     if list.count(i)>1:
#         list.remove(i)
        
        
# print(list)

