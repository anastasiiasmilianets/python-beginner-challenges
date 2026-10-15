import random

print("It's a number guessing game!")
print("")

top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print(f"Please type a number larger than {top_of_range} next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

secret_number = random.randint(1, top_of_range)
attempts = 0

print(f"Guess a number (between 1 and {top_of_range}):")

while True:
    attempts += 1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number")
        continue

    if user_guess < secret_number:
        print("Too low! Try a number higher than", user_guess)
    elif user_guess > secret_number:
        print("Too high! Try a number lower than", user_guess)
    else:
        print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
        break
