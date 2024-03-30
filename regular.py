class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res=0
        try:
            if divisor==0:
             res= dividend//divisor
        except :
            res= 0
        if dividend >=1 or dividend<0 :
                res=int(dividend//divisor)
        return res
my=Solution()
print(my.divide(int(input()),int(input())))