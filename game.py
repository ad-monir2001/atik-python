
"0/X PUZZLE GAME"




def Board(board):

    for row in range(3):
        print("   |".join(board[row * 3:(row + 1) * 3]))
        if row < 2:
            print("-" * 14)

def check_winner(board, player):

    winning_cell = [
        [0,1,2],[3,4,5],[6,7,8],  
        [0,3,6],[1,4,7],[2,5,8],  
        [0,4,8],[2,4,6]              
    ]
    return any(all(board[cell] == player for cell in combo) for combo in winning_cell)
   
def  full_board(board):

    return all(cell != " " for cell in board)

def PLAYERS(player):

    while True:
        try:
            p_c = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if p_c<10:
                return p_c
            else:
                print("out of range. enter a number between 1-9.")
        except ValueError as v:
            print("Invalid input. enter an integer number between 1-9.")

def main():
    board = [" " for _ in range(9)]
    player = "0"
    import random
    ran=["0","0"]
    ra=random.randint(0,1)
    r=ran[ra]
    while True:
        Board(board)
        move = PLAYERS(player)

        if board[move] == " ":
            board[move] = player
            if board[move]==r:
                board[move]=player
        else:
            print("this cell had already completed. Try again.")


        if check_winner(board, player):
            Board(board)
            print(f"Player {player} has won this game !")
            break


        player =r  if board[move] == "0" else "0"


main()
