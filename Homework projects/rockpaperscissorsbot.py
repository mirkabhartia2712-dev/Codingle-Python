import random

choices = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0

print("Welcome to Rock Paper Scissors!")
print("Type 'rock', 'paper', or 'scissors' to play")
print("Type 'quit' to exit the game")
print()

while True:
    player = input("Your choice: ").lower()
    
    if player == "quit":
        print(f"\nFinal Score - You: {player_score}, Computer: {computer_score}")
        print("Thanks for playing!")
        break
    
    if player not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue
    
    computer = random.choice(choices)
    
    print(f"Computer chose: {computer}")
    
    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win this round!")
        player_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1
    
    print(f"Score - You: {player_score}, Computer: {computer_score}")
    print()