import random

generated = random.randint(1, 100)

max_attempts = 3
attempts_used = 0

while attempts_used < max_attempts:
    print(generated)
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        if 1 <= guess <= 100:
            attempts_used += 1
            if guess == generated:
                print("\nCongratulations! \nYou guessed the number in " + str(attempts_used) + " attempts!")
                break
            elif guess > generated:
                print("Lower!")
            elif guess < generated:
                print("Higher!")
        else:
            print("Number must be between 1 and 100.")
    except ValueError:
        print("Please enter a whole number.")
else:
    print("Game over!")
    print(f"The generated number was {generated}!")