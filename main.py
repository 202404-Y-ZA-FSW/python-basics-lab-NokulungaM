import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Guess the number between 1 and 100:")

    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low.")
            elif guess > secret_number:
                print("Too high.")
            else:
                print(f"Correct! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")

number_guessing_game()
