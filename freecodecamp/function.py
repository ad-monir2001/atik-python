def main():
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


main()