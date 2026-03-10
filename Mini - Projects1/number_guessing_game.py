import random

number = random.randint(1, 10)

print("Guess the number between 1 and 10")

guess = int(input("Enter your guess: "))

if guess == number:
    print("Correct! You guessed the number.")
elif guess < number:
    print("Too low! The number was", number)
else:
    print("Too high! The number was", number)
