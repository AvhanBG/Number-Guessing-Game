import random
from stats import Stats

stats = Stats()
stats.load_stats()

while True:
    
    attempts = 0

    while True:
        try:
            minimum = int(input("Enter the minimum number: "))
            maximum = int(input("Enter the maximum number: ")) 
            if 0 < minimum < maximum: # checks if the minimum is greater than 0 and the maximum is greater than the minimum
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

    while attempts < max_attempts:
        try:
            guess = int(input(f"Guess a number between {minimum} and {maximum}: "))
            if minimum <= guess <= maximum:
                attempts += 1
                if guess == generated:
                    print("\nCongratulations! \nYou guessed the number in " + str(attempts) + " attempts!")
                    stats.record_win(attempts) 
                    stats.record_game(attempts)
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
        print(f"\nGame Over! \nThe generated number was {generated}!")
        stats.record_loss(attempts) 
        stats.record_game(attempts)

    stats.save_stats()

    play_again = input("Do you want to play again? (y/n) ").lower()
    
    if play_again != 'y':
        print("Thanks for playing!")
        stats.display_stats()
        break
    else:
        print("Starting a new game...")