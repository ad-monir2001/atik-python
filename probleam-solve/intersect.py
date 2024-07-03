


class Solution:
    def intersect(self, nums1:list[int], nums2: list[int]) -> list[int]:
        list1=[]
        for i in nums1:
            if i in nums2:
                if i not in list1:
                    list1.append(i)


        return list1
    
s=Solution()
print(s.intersect([1,2,2,1], [2,2]))
print(s.intersect([4,9,5], [9,4,9,8,4]))