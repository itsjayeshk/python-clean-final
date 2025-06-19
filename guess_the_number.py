import random
number_to_guess = random.randint(1,100)
guess = None
attempts = 0

print("Welcome to the number guesser game!!")
print("I am thinking a number between 1 and 100!")
while guess !=number_to_guess:
    guess = int(input("Enter the number which you are thinking "))
    attempts +=1

    if guess < number_to_guess:
        print("Too low!Try again a larger number :)")
    elif guess > number_to_guess:
        print("Too high!Try again a smaller number :)")  
    else:
        print(f"🎉 Correct! You guessed it in {attempts} attempts.")      