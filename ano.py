# def Board():
#     for i in range(3):
#         print("___|___|___")

# Board()
# def Main():
#     pass


def Board(board):

    for row in range(3):
        print("  |".join(board[row*3:(row+1)*3]))
        if row <3:
            print("--"*6)

def Players(player):


        while True:
            try:
                p_c=int(input("enter your choose  : "))-1
                if p_c<10:
                    return p_c
                else:
                    print("out of range;")
            except ValueError as v:
                print(v)
def Main():
    player="X"
    board=[" " for _ in range(9)]
    while True:
        Board(board)
        move=Players(player)
        if board[move]==" ":
            board[move]=player
        else:
            print("this is alra")
        player=" X" if board[move]==" 0" else " 0"
Main()