class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        l = list(zip(*strs))
        prefix = ""
        for i in l:
            if len(set(i))==1:
                prefix += i[0]
            else:
                break
        return prefix

                
s=Solution()
print(s.longestCommonPrefix(['flow','fl']))