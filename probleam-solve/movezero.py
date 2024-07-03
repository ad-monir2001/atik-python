class Solution:
    def moveZeroes(self, nums:list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if 0 in nums:
            result=nums.count(0)
            for i in range(result):
                nums.remove(0)
            for e in range(result):
                nums.append(0)
            return nums

        
s=Solution()

