import random

def start_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Guessing Game! I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Correct! You found it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid whole number.")

start_game()
