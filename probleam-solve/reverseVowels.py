class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        list1=[]
        list2=[]
        list3=[]
        list4=[]
        list5=[]
        list6=[]
        list7=[]
        list8=[]
        list9=[]
        for i in nums:
            if str(i).startswith('9'):
                list9.append(i)
            if str(i).startswith('8'):
                list8.append(i)
            if str(i).startswith('7'):
                list7.append(i)
            if str(i).startswith('6'):
                list6.append(i)
            if str(i).startswith('5'):
                list5.append(i)
            if str(i).startswith('4'):
                list4.append(i)
            if str(i).startswith('3'):
                list3.append(i)
            if str(i).startswith('2'):
                list2.append(i)
            if str(i).startswith('1'):
                list1.append(i)
        return list9+list8+list7+list6+list5+list4+list3+list2+list1
s=Solution()
print(s.largestNumber([3,30,8,7,65,90,25,34,5,9]))
print(s.largestNumber([3,30,34,5,9]))