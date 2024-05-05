class Solution:
    def removeElement(self, nums:list, val: int) -> int:

        
        a=[]
        nums.remove(val)
        for i in nums[val] :
            if i  not in a:
                a.append(i)
        return len(a)
    

A=Solution()
print(A.removeElement(list(map(int,input().split())),int(input())))