
def Board(board):
    for row in range(3):
        print("  |".join(board[row*3:(row+1)*3]))
        if row<3:
            print("-----------")

def Players(player):
    player=" 0"
    while True:
        try:
            p_c=int(input(f"choose {player} an int num 1-9 : "))-1
            if p_c<10:
                return p_c
            else:
                print("out of range ")
        except ValueError as v:
            print(v)
# def winner(win):
#     winning_value=[
#         [0,1,2],[3,4,5],[6,7,8],
#         [0,3,6],[1,4,7],[2,5,8],
#         [0,4,8],[2,4,6]
#     ]
#     for w in winning_value:
#         return w
    
    
def main():
    board=[" " for _ in range(9)]
    player=" 0"
    while True:
        Board(board)
        move=Players(player)
        if board[move]==" ": #see
            board[move]=player
        else:
            print("This cell had  already completed ")
        player='X' if board[move]==" 0" else " 0"
main()