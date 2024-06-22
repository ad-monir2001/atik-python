class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        list1=[]
        list2=[]
        for i in range(1,a+1):
            if a%i==0:
                list1.append(i)
                
                
        for e in range(1,b+1):
            if b%e==0:
                list2.append(e)
        set1=set(list1) 
        set2=set(list2)
        
        return len(set1.intersection(set2))

s=Solution()
print(s.commonFactors(30,25))

# a=30
# s=25
# list1=[]
# list2=[]
# for i in range(1,a+1):
#     if a%i==0:
#         list1.append(i)
        
        
# for e in range(1,s+1):
#     if s%e==0:
#         list2.append(e)
# set1=set(list1) 
# set2=set(list2)
# print(len(set1.intersection(set2)))     
