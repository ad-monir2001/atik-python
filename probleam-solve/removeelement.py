class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        list1=[]
        list2=[]
        if len(num)>=1 and len(num)<=10**4:
            for i in num:
                list1.append(str(i))
            e=int(''.join(list1))+k
            s=str(e)
            for j in s:
                list2.append(int(j))

            return list2

