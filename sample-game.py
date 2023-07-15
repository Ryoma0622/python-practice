import random

def main():
    number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        if guess < 1 or guess > 100:
            print("Your guess is out of range. Please guess again between 1 and 100.")
            continue

        attempts += 1

        if guess < number:
            print("Higher!")
        elif guess > number:
            print("Lower!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

    play_again = input("Would you like to play again? (y/n): ")
    if play_again.lower() == 'y':
        main()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    main()
