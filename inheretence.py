# class Solution:
#     def removeElement(self, nums:list, val: int) -> int:

        
#         a=[]
#         nums.remove(val)
#         for i in nums[val] :
#             if i  not in a:
#                 a.append(i)
#         return len(a)
    

# A=Solution()
# print(A.removeElement(list(map(int,input().split())),int(input())))
# import random

# # Function to print the game board
# def print_board(player_pos, enemy_pos, board_size):
#     for i in range(board_size):
#         for j in range(board_size):
#             if (i, j) == player_pos:
#                 print('@', end=' ')
#             elif (i, j) == enemy_pos:
#                 print('E', end=' ')
#             else:
#                 print('.', end=' ')
#         print()

# # Function to move the player
# def move_player(direction, player_pos, board_size):
#     x, y = player_pos
#     if direction == 'up':
#         x = max(0, x - 1)
#     elif direction == 'down':
#         x = min(board_size - 1, x + 1)
#     elif direction == 'left':
#         y = max(0, y - 1)
#     elif direction == 'right':
#         y = min(board_size - 1, y + 1)
#     return (x, y)

# # Function to move the enemy
# def move_enemy(enemy_pos, board_size):
#     directions = ['up', 'down', 'left', 'right']
#     direction = random.choice(directions)
#     return move_player(direction, enemy_pos, board_size)

# # Main function to run the game
# def main():
#     board_size = 5
#     player_pos = (0, 0)
#     enemy_pos = (board_size - 1, board_size - 1)

#     print("Welcome to the Chase Game!")

#     while True:
#         print_board(player_pos, enemy_pos, board_size)

#         # Get player input
#         direction = input("Enter direction (up/down/left/right): ").lower()
        
#         # Move player
#         player_pos = move_player(direction, player_pos, board_size)

#         # Move enemy
#         enemy_pos = move_enemy(enemy_pos, board_size)

#         # Check if player and enemy occupy the same position
#         if player_pos == enemy_pos:
#             print_board(player_pos, enemy_pos, board_size)
#             print("Game over! You were caught by the enemy.")
#             break

# if __name__ == "__main__":
#     main()
# /* Board.py
# /* Square.py
