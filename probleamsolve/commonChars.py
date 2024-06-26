# rules  no 1
# from functools import reduce
# from typing import Counter


# class Solution:
    
#     def commonChars(self, words: list[str]) -> list[str]:
#         return list(reduce(lambda a, b: a & b, map(Counter, words)).elements())

# rules no 2

import collections
class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        ans=collections.Counter(words[0])
        for word in words:
            ans &=collections.Counter(word)
        return list(ans.elements())    


S=Solution()
print(S.commonChars(["bella","label","roller"]))