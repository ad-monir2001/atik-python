
# import turtle as t
# import random
# t.shape("turtle")
# t.speed(0)
# t.bgcolor("black") 
# a=0
# for x in range(350): 
#     a=a+1
#     # t.pencolor(colors[x%6]) 
#     t.pencolor('#%06x' % random.randint(0, 2**24 - 1))
#     t.width(a//180 + 1) 
#     t.forward(x) 
#     t.right(59)
# t.goto(0,0)
# t.write("Atikur",align="center",font=("",150,""))
# t.done()

# import turtle as t
# t.bgcolor("black")
# t.speed(0)
# t.color("cyan")
# angle = 0
# for _ in range(100):
#     t.forward(angle)
#     t.right(12)
#     angle = angle+1
# t.done()
# def print_board(board):
#     print("  0 1 2")
#     for i in range(3):
#         print(f"{i} {' '.join(board[i])}")

# def check_winner(board, player):
#     for i in range(3):
#         # Check rows
#         if all(cell == player for cell in board[i]):
#             return True
#         # Check columns
#         if all(board[j][i] == player for j in range(3)):
#             return True
#     # Check diagonals
#     if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
#         return True
#     return False

# def main():
#     board = [[' ' for _ in range(3)] for _ in range(3)]
#     current_player = 'X'
#     print("Welcome to Tic-Tac-Toe!")
#     print("Instructions: Enter the row and column where you want to place your mark (0-2).")
#     print_board(board)

#     for turn in range(9):
#         print(f"\nPlayer {current_player}'s turn")
#         row, col = map(int, input("Enter row and column (e.g., 1 2): ").split())
#         if board[row][col] == ' ':
#             board[row][col] = current_player
#             print_board(board)
#             if check_winner(board, current_player):
#                 print(f"Player {current_player} wins!")
#                 return
#             current_player = 'X' if current_player == 'O' else 'O'
#         else:
#             print("That cell is already occupied. Try again.")

#     print("It's a draw!")

# if __name__ == "__main__":
#     main()
