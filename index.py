import random

choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)

print("Let's play rock, paper, or scissors")
player_choice = input("Choose rock, paper, or scissors: ").lower()

print(f"Computer chose: {computer_choice}")

# Initialize winner variable
winner = None

# Determine the winner
if (player_choice == "rock" and computer_choice == "scissors") or \
   (player_choice == "scissors" and computer_choice == "paper") or \
   (player_choice == "paper" and computer_choice == "rock"):
    winner = "Player"
elif player_choice == computer_choice:
    winner = "Tie"
else:
    winner = "Computer"

# Print the result
if winner == "Player":
    print("You won!")
elif winner == "Computer":
    print("Computer won!")
else:
    print("It's a tie!")
