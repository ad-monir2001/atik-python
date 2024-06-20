# class Solution:
#     def nextGreaterElement(self, n: int) -> int:
        
#         list1=[]
#         str1=str(n)
#         for i in str1:
#             list1.append(i)
#         list1.reverse()
#         if 0 not in list1:
#             reverstin_str=''.join(list1)
#             int_str=int(reverstin_str)
#             if int_str>n:
#                 return int_str
#             else:
#                 return -1
#         if 0 in list1:
#             pass
# s=Solution()
# print(s.nextGreaterElement(12))






class Solution:
    def nextGreaterElement(self, n: int) -> int:
        list1=[]
        for i in str(n):
            list1.append(i)
        list1.sort(reverse=True)
        join_list=''.join(list1)
        int_join_list=int(join_list)
        if int_join_list>n:
            return int_join_list
        else:
            return -1
        
s=Solution()
print(s.nextGreaterElement(101))

a=[2,3,6,9]
a.sort()
print(a)
print(eval("456"+"77"))
