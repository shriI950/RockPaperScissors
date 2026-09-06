import random

print("Welcome to game of Rock, Paper, Scissors!!!")

print("1 is for '✊' (Rock).")
print("2 is for '✋' (Paper).")
print("3 is for '✌️' (Scissors).")

options = ['✊', '✋', '✌️']
player = int(input("Select number between 1 to 3: "))
computer = random.randint(1,3)

if player==computer:
  print("It's a tie!")
else:
  if player==1:
    if computer==2:
      print("The computer won!")
    else:
      print("The player won!")
  elif player==2:
    if computer==1:
      print("The player won!")
    else:
      print("The Computer won!")
  else:
    if computer==1:
      print("The computer won!")
    else:
      print("The player won!")
