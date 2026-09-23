import random

while True:
    attempts_used = 0
    while True:
        try:
            minimum = int(input("Enter the minimum number: "))
            maximum = int(input("Enter the maximum number: "))
            if 0 < minimum < maximum:
                break
            else:
                print("Minimum number must be greater than 0, and less than the maximum.")
        except ValueError:
            print("Invalid input. Please enter whole numbers.")
    while True:
        try:
            max_attempts = int(input("Enter the maximum number of attempts: "))
            if max_attempts > 0:
                break
            else:
                print("Attempts must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a whole number greater than 0.")

    generated = random.randint(minimum, maximum)

    while attempts_used < max_attempts:
        try:
            guess = int(input(f"Guess a number between {minimum} and {maximum}: "))
            if minimum <= guess <= maximum:
                attempts_used += 1
                if guess == generated:
                    print("\nCongratulations! \nYou guessed the number in " + str(attempts_used) + " attempts!")
                    break
                elif guess > generated:
                    print("Lower!")
                elif guess < generated:
                    print("Higher!")
            else:
                print(f"Your guess must be between {minimum} and {maximum}.")
        except ValueError:
            print("Please enter a whole number.")
    else:
        print("Game over!")
        print(f"The generated number was {generated}!")

    play_again = input("Do you want to play again? (y/n)" ).lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break
    else:
        print("Starting a new game...")