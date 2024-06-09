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
print(re.findall(r'(\w+land*)',text3)) # it use to find some especial element from the string
print(re.search("england",text3))


text4='Bangladesh is an agricultural country Bangladeshi man is great and populated'
print(re.findall(r'(B\w+i)',text4)) #its print which word started with B and end in i ,
print(re.findall(r'(B.+i)',text4)) # its return which word started with B and it will stop in where  its find last h In this sentence.

print(re.findall(r'(B.+?h)',text4))

re=re.search(r"(B.+?h)",text4)
print(re.group())

# DIGIT AR CHETRE

