import random


def play_game():
    secret_number = random.randint(1, 10)
    max_attempts = 3
    attempts = 0
    guesses = []

    print("\n--- New Game ---")
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: "))
        except ValueError:
            print("Please enter a valid number")
            continue

        guesses.append(guess)
        attempts += 1

        if guess == secret_number:
            print("Correct! You won!")
            print(f"Your guesses were: {guesses}")
            return True
        elif guess > secret_number:
            print("Too high")
        else:
            print("Too low")

    print(f"Game Over! The number was {secret_number}")
    print(f"Your guesses were: {guesses}")
    return False


while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again != "yes":
        print("Goodbye!")
        break
