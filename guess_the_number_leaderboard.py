import random

high_score = None

print("Welcome to 'Guess the Number'!")
print("Try to guess the number in the least attempts!")

while True:
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guess = None

    while guess != number_to_guess:
        try:
            guess = int(input("Enter your guess (1-100): "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low. Try again.")
            elif guess > number_to_guess:
                print("Too high. Try again.")
            else:
                print(" Correct! You guessed it in {attempts} attempts.")

                if high_score is None or attempts < high_score:
                    high_score = attempts
                    print(" New High Score: {high_score} attempts!")
                else:
                    print("Current High Score: {high_score} attempts.")
        except ValueError:
            print(" Please enter a valid number!")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break





