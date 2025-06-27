name1 = input("Enter your name: ")
name2 = input("Enter your partner's name: ")

lover = (name1 + name2).lower()  # Fixed: Now it actually converts to lowercase

true_count = 0
for letter in "true":
    true_count += lover.count(letter)

love_count = 0
for letter in "love":
    love_count += lover.count(letter)

score = int(str(true_count) + str(love_count))

print("Your score is:")
print(score)

if score < 10 or score > 90:
    print("You go together like coke and mentos!")
elif 40 <= score <= 50:
    print("You're alright together.")
else:
    print("Meh, it's okay-ish.")

