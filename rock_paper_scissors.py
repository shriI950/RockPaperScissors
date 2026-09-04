import random

print("Welcome to game of Rock, Paper, Scissors!!!")

print("1 is for '✊' (Rock).")
print("2 is for '✋' (Paper).")
print("3 is for '✌️' (Scissors).")

options = ['✊', '✋', '✌️']
player = int(input("Select number between 1 to 3: "))
computer = random.randint(1,3)

print(f'You chose: {options[player-1]}')
print(f'CPU chose: {options[computer-1]}')

