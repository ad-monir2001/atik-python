


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2!=str2+str1:
            return ''

        a = len(str1)
        b = len(str2)
        while b != 0:
            a , b = b, a%b
        return str2[:a]
    
    
s=Solution()
