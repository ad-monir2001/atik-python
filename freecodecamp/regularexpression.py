# import re
# e=input('email; ')
# print(re.findall(r'.+@.+\s*[.\w]+\s*\w+',e))
# for i in range(5):
#     import re
#     e=input('enter your email : ')
#     if re.search(r'(^\w+@\w+\.\w+$)',e):
#         print('v')
#     else:
#         print('In')

for i in range(4):
    e=input('enter your email ')
    import re
    if re.search(r'^[^@]+@.+\.\w+$',e):
        print('valid')
    else:
        print('InValid')
# import re
# em='atikur@email.com , atikur@email@.com, atikur@email.com. , atikur@email.com@ , atikur (at) email dot com'
# print(re.findall(r'^\w+@\w+\.\w+$',em))

# import re
# a='Abcd 123456 -- 0'
# print(re.sub(r'\d','0',a))
# # sub method is use for replace anything 
# em='book at Atikur.com , book At atikur.com , book (at) atik dot com , book [at] atikur [dot] com '

# print(re.sub(r'(\s+[\(\[]*\s*at\s*[\)\]]*\s+)','@',em,flags=re.IGNORECASE))
# date='hello i am atikur Rahman 2024-10-10  2024/10/09  11/12/2024 Now i am leanring programming'

# d1=(r'\d{4}[\s*/-]\d{2}[\s*/-]\d{2}')
# d2=(re.compile(r'(\d{4})[\s*/-](\d{2})[\s*/-](\d{2})'))
# alt=re.compile(r'(\d{2})[\s*/-](\d{2})[\s*/-](\d{4})')

# print(re.sub(d2,r'\3-\2-\1',date))
# print(re.sub(alt,r"\g<3>-\3-\g<2>-\g<1>",date))

# email="Email1 : book@subben.com , thank you book@subben ,py.book@subben.com"
# print(re.findall(r'(\w+@\w+[.]\w+)',email))
# print(re.findall(r'(\w+@\w+\.\w+)',email))
# print(re.findall(r'([.\w]+@\w+[.]\w+)',email))

# em='book at Atikur.com,book At atikur.com , book (at) atik dot com,book[at] atikur [dot] com .'
# print(re.sub(r'(\s*[\(\[]*\s*at\s*[\)\]]*\s+)','@',em,flags=re.IGNORECASE))
# htm = '<li>Bangladesh</li><li>England</li><li>Australia</li>'
# print(re.findall(r'<li>(.*?)</li>',htm))
# print(re.findall(r'<li>.*?</li>',htm))


# e=('https://app.netlify.com/ , https://www.hackerrank.com/ ,https://leetcode.com/,https://translate.google.com.bd/')                      
# import re
# print(re.findall(r'\w+[\:\/]+\w+\.\w+\.\w+\/',e))#only for 2 dots and 3 WORD
# r=re.compile(r'\w+[.\:\/\w]+')
# print(re.findall(r,e))
# pri=(re.split(r'\w+', 'Words words words', 3))
# prin=(re.split(r'\W+', 'Words words words', 3))
# m = re.match(r"(?P<f_n>\w+) (?P<L_N>\w+)", "Malcolm Reynolds")
# print(m.group('f_n','L_N'))

# email = "tony@tiremove_thisger.net"
# m = re.search("remove_this", email)
# email[:m.start()] + email[m.end():]
# 'tony@tiger.net'
