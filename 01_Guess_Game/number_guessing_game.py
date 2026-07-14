import random

print("It's a number guessing game!")
print("")

secret_number = random.randint(1, 100)
attempts = 0

print("Guess a number (between 1 and 100):")

while True:
    user_guess = int(input())
    attempts += 1
    if user_guess < secret_number:
        print("Too low! Try a number higher than", user_guess)
    elif user_guess > secret_number:
        print("Too high! Try a number lower than", user_guess)
    else:
        print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
        break
