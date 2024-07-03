class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:

        list2=[]
        if len(b)>len(a):
            for i in a:
                if i in b:
                    list2.append(i)
                    print(list2)
            return len(list2)
        
        if len(b)<len(a):
            return -1
        
        
s=Solution()
print(s.repeatedStringMatch('abcd','cdabcdab'))