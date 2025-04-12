

import random

actions = ["rock", "paper", "scissors"]

def game(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "scissors" and computer_choice == "paper") or \
       (user_choice == "paper" and computer_choice == "rock"):
        return "win"
    return "loss"

def main():

    wins = 0
    losses = 0
    ties = 0

    while (1):

        
        computer_choice = random.choice(actions)
        user_input = input("Enter Rock, Paper, Scissors (or Quit) :\n")
        user_choice = user_input.lower()
        
        if user_choice == "quit":
            break
        
        if user_choice not in actions:
            print("Invalid choice, try again.\n")
            continue

        print("You chose:", user_choice)
        print("Computer chose:", computer_choice)

        result = game(user_choice, computer_choice)

        if result == "win":
            print("You win :)")
            wins += 1
        elif result == "loss":
            print("You lose :(")
            losses += 1
        else:
            print("A tie :|")
            ties += 1

        print("Score")
        print("You: ", wins, "Computer: ", losses, "Ties: ", ties, "\n")

if __name__ == "__main__":
    main()
