# class Solution:
#     def halvesAreAlike(self, s: str) -> bool:
#         list1=[]
#         list2=[]
#         m=len(s)//2
#         voiel=['a','e','i','o','u','A','E','I','O','U']
#         for i in range(m):
#             for j in voiel:
#                 if s[i]==j:
#                     list1.append(s[i])

#         for e in range(m,len(s)):
#             for j in voiel:
#                 if s[e]==j:
#                     list2.append(s[e])
                    
#         return list1,list2
    
    
# s=Solution()
# print(s.halvesAreAlike("book"))


# a={0,7,7}
# print(a)

class Solution:
    def secondHighest(self, s: str) -> int:
        list1=[]
        for i in s:
            if i.isdigit():
                list1.append(i)

        list1.sort()
        list2=[]
        for e in list1:
            if e not in list2:
                list2.append(e)
                
        list2.sort()
        return int(list2[-2])
        
        
s=Solution()
print(s.secondHighest("dfa12321afd"))