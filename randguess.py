import random

number = random.randrange(0, 100)
guessCheck = "wrong"
attempts = 0  # Initialize the counter
print("Welcome to Number Guess")

while guessCheck == "wrong":
    response = input("Please input a number between 0 and 100:")
    try:
        val = int(response)
    except ValueError:
        print("This is not a valid integer. Please try again")
        continue
    val = int(response)
    if val < number:
        print("This is lower than the actual number. Please try again.")
    elif val > number:
        print("This is higher than the actual number. Please try again.")
    else:
        print("This is the correct number")
        guessCheck = "correct"
    attempts += 1  # Increment the counter

print("Thank you for playing Number Guess. See you again")
print("Number of attempts:", attempts)  # Print the number of attempts
