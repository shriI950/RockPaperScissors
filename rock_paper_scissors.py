import random

print("Welcome to game of Rock, Paper, Scissors, Lizard, Spock!!!")

print("1 is for '✊' (Rock).")
print("2 is for '✋' (Paper).")
print("3 is for '✌️' (Scissors).")
print("4 is for '🦎' (Lizard).")
print("5 is for '🖖' (Spock).")

options = ['✊', '✋', '✌️', '🦎', '🖖']
player_won = False # Program runs till Player wins!

while not player_won:
  player = int(input("Select number between 1 to 5: "))
  computer = random.randint(1,5)
  
  print(f"You chose: {options[player-1]}")
  print(f"CPU chose: {options[computer-1]}")
  
  
  if player==computer:
    print("It's a tie!")
  else:
    if player==1:
      if computer==2 or computer==5:
        print("The computer won!")
      else:
        print("The player won!")
        player_won=True
    elif player==2:
      if computer==3 or computer==4:
        print("The computer won!")
      else:
        print("The player won!")
        player_won=True
    elif player==3:
      if computer==1 or computer==5:
        print("The computer won!")
      else:
        print("The player won!")
        player_won=True
    elif player==4:
      if computer==1 or computer==3:
        print("The computer won!")
      else:
        print("The player won!")
        player_won=True
    else:
      if computer==4 or computer==2:
        print("The computer won!")
      else:
        print("The player won!")
        player_won=True
