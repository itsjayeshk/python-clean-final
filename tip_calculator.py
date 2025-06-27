bill = float(input("What was the total bill: "))
tip = float(input("What is the tip percentage: "))
people = float(input("How many people are splitting the bill: "))
percentage = 100 + tip
actualbill = (bill * percentage) / 100
perhead = actualbill / people
print("The amount which has to be paid by per person is ")
print(perhead)
