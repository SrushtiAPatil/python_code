import random

number = random.randint(1, 100)
guess = 0
attempts = 0

print("Guess a number between 1 and 100")

while guess != number:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess > number:
        print("Too High!")
    elif guess < number:
        print("Too Low!")
    else:
        print("Correct! Attempts:", attempts)
