
email=input('Enter your email ').strip()

    
username,domain=email.split('@')
print(username)
print(domain)
if username :
    print('Valid')
else:
    print('INvalid')