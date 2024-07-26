class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        if x>=y:
            x1=bin(x).replace("0b","")
            p=len(x1)
            y1=bin(y).replace("0b","").zfill(p)
        else:
            y1=bin(y).replace("0b","")
            p=len(y1)
            x1=bin(x).replace("0b","").zfill(p)
        x1=list(x1)
        y1=list(y1)
        res=0
        for i in range(len(x1)):
            if x1[i]!=y1[i]:
                res=res+1
        return res
    
s=Solution()
print(s.hammingDistance(1,4))
    
