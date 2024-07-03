class Solution:
    def hammingWeight(self, n: int) -> int:
        def bit(n,count):
            if n==0:
                return 0
            if n%2==0:
                return bit(n//2,0)
            else:
                return bit(n//2,1)

        return bit(n,0)
    
    
s = "A man, a plan, a canal: Panama"   
print(all(s[i]==s[~i] for i in range(len(s)//2)))125