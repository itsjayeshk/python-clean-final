while True:
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

    option = input("Do you want to continue? (y/n): ")
    if option.lower() != "y":
        print("Goodbye!")
        break
