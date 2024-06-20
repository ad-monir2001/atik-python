

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        list2=[]
        for i in nums:
            if nums.count(i)==2:
                list2.append(i)
                
        return len(list2)>1
    
s=Solution()
print(s.containsDuplicate([1,2,3,1]))


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums))!=len(nums)