class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        f=s.split()
        return ' '.join(f[:k])
    
s=Solution()
print(s.truncateSentence("Hello how are you Contestant", 4))