

# class Solution:
#     def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         list1=[]
        
#         for e in range(m):
#             list1.append(nums1[e])
#         for i in range(n):
#             list1.append(nums2[i])
            
#         return list1
    
    
# s=Solution()
# print(s.merge([1,2,3,0,0,0],3,[2,5,6],3))

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1[m:] = nums2
        nums1.sort()