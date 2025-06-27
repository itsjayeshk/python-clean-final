print("Welcome to the treasure game, where you have to make the right choices to win!")
print("First Game!")

a = input("Do you want to go left or right? ")
direction = a.lower()

if direction == "left":
    b = input("Do you want to swim in the river or wait? ")
    decision = b.lower()
    
    if decision == "wait":
        c = input("Which door do you want to choose? Red / Blue / Yellow? ")
        color = c.lower()
        
        if color == "red":
            print("Burnt in fire! Game Over!")
        elif color == "blue":
            print("Eaten by beasts! Game Over!")
        elif color == "yellow":
            print("🎉 Congratulations! You found the treasure and won the game!")
        else:
            print("Wrong door! Game Over!")
    else:
        print("Attacked by crocodiles! Game Over!")
else:
    print("Fell into a pit! Game Over!")
