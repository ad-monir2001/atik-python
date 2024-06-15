try:
    x=int(input('what is x?'))
    print(f'x is {x}')
except ValueError as V:

    print(V)
    print('\n')