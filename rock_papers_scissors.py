import random

choices = ["rock", "paper", "scissors"]
hand = input("Enter your choice (rock/paper/scissors): ").lower()
computer_choice = random.choice(choices)

print(f"Computer chose: {computer_choice}")

if hand == computer_choice:
    print("It's a tie!")
elif (
    (hand == "rock" and computer_choice == "scissors") or
    (hand == "paper" and computer_choice == "rock") or
    (hand == "scissors" and computer_choice == "paper")
):
    print("You win!")
else:
    print("You lose!")

