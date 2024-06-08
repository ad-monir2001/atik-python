import re



text='My name is Atikur , Atikur is the best  Boy'
#function of regular expression
# findall
# search
# split
# sub
a=re.findall('[A-D]',text) #this method is needed for searching any small or capital letter in any variable with a range. Range is always string.
print((list(set(a))))

text2='Now I am learning python programming language'
s=re.findall('^Now',text2)# find first word or letter or i can use $ to search the last word or letter 
print(s)