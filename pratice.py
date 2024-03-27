# import re
# a="phone:+8801784 040029,+6501321-544143,01235152,+9901721-794952,+8801829 -236514"
# p=(re.findall(r"01[35879]\d{2}\-*\s*\d{6}",a))
# print(p)

# import turtle as t
for i in range(2):
    t.begin_fill()
    t.color("green","green")
    t.forward(200)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.end_fill()

t.color("green")
t.right(45)
t.forward(110)
t.begin_fill()
t.color("red","red")
t.circle(26.6190379)
t.end_fill()
t.exitonclick()

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) :
#         self.s=s
#         self.a=[]
#     def count(self):

#         print(len(set(self.s)))


# my=Solution()
# my.s=input()
# a=[]
# for i in my.s:
#     if i not in a:
#         a.append(i)
# print(len(a))
# my.count()
