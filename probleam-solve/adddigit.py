class Solution:
    def addDigits(self, num: int) -> int:
        return num%9 if num%9!=0 or num==0 else 9
                


s=Solution()
print(s.addDigits(40))
