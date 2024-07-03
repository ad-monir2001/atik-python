class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        eval1=eval(num1)
        eval2=eval(num2)
        return str(int(eval1+eval2))
    
s=Solution()
print(s.addStrings("123","54"))
# 415
# 434