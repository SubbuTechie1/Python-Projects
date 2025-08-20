import random
number = random.randint(1,100)
attempts =0
max_attempts = 7
print("Guess the Number (1,100):")
while attempts < max_attempts:
    try:
        guess = int(input(f"Attemput {attempts+1}: Enter your Guess:"))
        attempts += 1
        if guess == number:
            print("Correct! You guessed the correct Number")
            break
        elif guess < number:
            print("Too Low")
        else:
            print("Too High")
    except ValueError:
        print("Plese Enter the correct Number")
if attempts == max_attempts and guess != number:
    print(f"Out of Attempts, the cirrect number is {number}")
