class Solution:
    def countSegments(self, s: str) -> int:
        list1=list(map(str,s.split()))
        
        
        return len(list1)
    
s=Solution()
print(s.countSegments("hello  my name is Atikur Rahman"))