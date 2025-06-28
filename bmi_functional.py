def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def check_bmi(bmi):
    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi < 25:
        print("Normal weight")
    elif 25 <= bmi < 30:
        print("Overweight")
    else:
        print("Obese")

while True:
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is: {bmi:.2f}")
    check_bmi(bmi)

    choice = input("Do you want to continue another BMI? (y/n): ").lower()
    if choice == "n":
        print("Thank you!")
        break
