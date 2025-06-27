weight = float(input("Enter your weight in kgs: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height * height)
print("Your BMI is " + str(bmi) + "!")

if bmi < 18.5:
    print("You are underweight!")
elif 18.5 <= bmi < 25:
    print("You are normal!")
elif bmi < 30:
    print("You are overweight!")
else:
    print("You are obese!")



