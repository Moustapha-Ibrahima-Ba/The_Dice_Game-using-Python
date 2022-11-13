# --------------- VERSION 1 ---------------

# import random
import random

# Give name to players
player1 = input("Player 1, What is your name ? ")
print()
player2 = input("Player 2, What is your name ? ")

# Pick a random number between 1-6 for each player

player1_num = random.randint(1, 6)
print(f" {player1}, you pick {player1_num} ")

player2_num = random.randint(1, 6)
print(f" {player2}, you pick {player2_num} ")

# Who wins ?
if player1_num == player2_num:
    print(f"Nobody wins, you pick the same number which happens to be {player1_num}")
elif player1_num > player2_num:
    print(f"Therefore...{player1}, you win. Congratulation!")
else:
    print(f"Therefore...{player2}, you win. Congratulation!")
