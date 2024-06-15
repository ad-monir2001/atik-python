def maine():
    x=int(input('enter your number : '))
    if even(x):
        print(f'{x} is even number ')
    else :
        print(f'{x} is odd number ')

def even(a):
    if a%2==0:
        return True
    else:
        return False
    #rule2
    return True if a%2==0 else False
    #rule3
    return (a%2==0)


maine()





for i in range(3):
    for _ in range(3):
        print("#",end='',)
    print()



def main():
    print_square(3)
    
def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#",end="")
        print()
        
main()  



def get_error():
    pass