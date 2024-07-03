# class Solution:
#     def reverseWords(self, s: str) -> str:
#         return ' '.join(map(lambda word: word[::-1], s.split()))

# class Solution:
#     def reverseWords(self, s: str) -> str:
#         words = s.split(" ")
#         return " ".join(word[::-1] for word in words)    

# class Solution:
#     def reverseWords(self, s: str) -> str:
#         l=s.split(" ")
#         for i in range(len(l)):
#             l[i]=l[i][::-1]
#         return " ".join(l)
         
class Solution:
    def reverseWords(self,s:str)->str:
        list1=[]
        split1=s.split()
        for i in range(len(split1)):
            res=split1[i][::-1]
            list1.append(res)
        return ' '.join(list1)
        
s=Solution()

