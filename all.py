


def Board(board):

    for row in range(3):
        print("  |".join(board[row*3:(row+1)*3]))
        if row<3:
            print("-"*11)
    



def Players(player):

    while True:
        try:
            p_c=int(input("choose an  :"))-1
            if p_c<10:
                return p_c
            else:
                print("out of index")
                
        except ValueError as v:
            print(v)

def Wining(board,player):
    wining_c=[
        [0,1,2],[3,4,5],[6,7,8],  
        [0,3,6],[1,4,7],[2,5,8],  
        [0,4,8],[2,4,6]              
    ]
    
    return(any(all(board[cell]==player for cell in i)for i in wining_c))




def main():
    player="X"
    board=[" " for _ in range(9)]

    while True:
        Board(board)
        move=Players(player)
        if board[move]==" ":
            board[move]=player
        else:
            print("this is already completed")


        if Wining(board, player):
            Board(board)
            print(f"Player {player} has won this game !")
            break

        player="0" if board[move]=="X" else "X"



main()


