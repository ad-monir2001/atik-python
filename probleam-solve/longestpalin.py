# class Solution:
#     def triangleType(self, nums: list[int]) -> str:    
#         nums.sort()
#         if not (nums[0] + nums[1] > nums[2] and nums[0] + nums[2] > nums[1] and nums[2]+ nums[1] > nums[0]):
#             return 'none'              
#         if nums[0] == nums[1] ==nums[2]:
#             return 'equilateral'
#         elif nums[0] != nums[1] != nums[2]:  
#             return 'scalene'
#         else:
#             return 'isosceles'
        
# v=Solution()
# print(v.triangleType([8,4,2]))



# class Solution:
#     def triangleType(self, nums: List[int]) -> str:
#         a = nums[0]
#         b = nums[1]
#         c = nums[2]
#         if a+b>c and b+c>a and a+c>b:
#             if a==b and b==c:
#                 return "equilateral"

#             elif a==b or a==c or b==c:
#                 return "isosceles"
#             else:
#                 return "scalene"
#         else:
#             return "none"
        
        
class Solution:
    def triangleType(self, nums: list[int]) -> str:
        if nums[0]+nums[1]>nums[2] and nums[0]+nums[2]>nums[1] and nums[1]+nums[2]>nums[0]:
            if len(set(nums))==1:
                return "equilateral"
            elif len(set(nums))==2:
                return "isosceles"
            else:
                return "scalene"
        else:
            return "none"