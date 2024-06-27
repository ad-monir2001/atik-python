class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left=0
        right=len(nums)-1

        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                left=mid+1
            if nums[mid]>target:
                right=mid-1

        return -1
    
    
s=Solution()
print(s.search([4,5,6,7,0,1,2],0))