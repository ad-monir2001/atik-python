class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res=0
        try:
            pass
        except ZeroDivisionError:
            res=dividend/divisor
            return res==0
        if (dividend >=0 or dividend<=0) and divisor!=0:
                res=int(dividend/divisor)
        return res
my=Solution()
print(my.divide(int(input()),int(input())))