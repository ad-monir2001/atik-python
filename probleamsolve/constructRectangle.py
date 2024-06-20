class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        list1=[]
        length=0
        for i in range(1,area):
            s=length+1
            if area == i **2 :
                list1.append(i)
                list1.append(i)
                
            if area == i*length:
                
                list1.append(length)
                list1.append(i)
        return list1
    
s=Solution()
print(s.constructRectangle(4))