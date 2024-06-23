import re



text='My name is Atikur , Atikur is the best  Boy'
#function of regular expression
# findall
# search
# split
# sub
# a=re.findall('[A-D]',text) #this method is needed for searching any small or capital letter in any variable with a range. Range is always string.
# print((list(set(a))))

# text2='Now I am learning python programming language'
# s=re.findall('^Now',text2)# find first word or letter or i can use $ to search the last word or letter 
# print(s)

text3="england , ireland , finland , new ze land , poland , BAngladesh , pakistan"
print(0,re.findall(r'(\w+land*)',text3)) # it use to find some especial element from the string

print()

text4='Bangladesh is an agricultural country Bangladeshi man is great and populated'
print(1,re.findall(r'(B\w+)',text4)) #its print which word started with B and end in i ,
print()
print(2,re.findall(r'(B.+i)',text4)) # its return which word started with B and it will stop in where  its find last h In this sentence.
print()
print(re.findall(r'(B.+?h)',text4))
print()
re=re.search(r"(B.+?h)",text4)
print(re.group())

# DIGIT AR CHETRE

digit='Atikur:01784 040029, Monir:01321-544143, None: 00000 111111'
import re
# res=re.compile(r'\d{5}\s*\d{6}')
res=re.compile(r'01[356789]\d{2}[-]\d{6}')
print(res.findall(digit))
