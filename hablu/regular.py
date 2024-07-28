import re

text='My name is Atikur , Atikur is the best  Boy'

# findall
# search
# split
# sub
a=re.findall('[A-D]',text) #this method is needed for searching any small or capital letter in any variable with a range. Range is always string.
# print(a)

# find first word or letter or i can use $ to search the last word or letter 
# print(s)

text3="england , ireland  , new ze land , poland , BAngladesh , pakistan ,finland , Netherlands"

print(re.findall(r'([\w\s*]+land)',text3))

text4='Bangladesh is an agricultural country Bangladeshi man is great and populated'
# print(1,re.findall(r'(B\w+)',text4)) #its print which word started with B and end in i ,

# print(2,re.findall(r'(B.+i)',text4)) # its return which word started with B and it will stop in where  its find last h In this sentence.
# print()
# print(re.findall(r'(B.+?h)',text4))
# print()
# re=re.search(r"(B.+?h)",text4)
# print(re.group())
