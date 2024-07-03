class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        li1 = []
        li2 = []
        for i in range(len(s)):
            if s[i] in vowels:
                li1.append(s[i])
                li2.append(i)
        for j in range(len(li2)):
            s = s[:li2[j]] + li1[-j-1] + s[li2[j]+1:]
        return s
s=Solution()
print(s.reverseVowels("hello"))