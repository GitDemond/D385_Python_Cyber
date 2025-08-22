import random

# Generate a random number
number = random.randint(1, 20)
#Testing win condition print(number)
guesses = 0
guessesMax = 3

print("Guess a number between 1 and 20. You have 3 tries!")

while guesses < guessesMax:
    try:
        userGuess = int(input("Please guess a number between 1 & 20. >> "))
        
        # Validate input range
        if not (1 <= userGuess <= 20):
            raise ValueError("Your guess must be between 1 and 20.")
        
        guesses += 1
        guessesLeft = guessesMax - guesses

        if userGuess == number:
            print("You Win! You guessed the correct number!!")
            break
        else:
            if guessesLeft > 0:
                print(f"Sorry, not correct. {guessesLeft} guesses left.")
            else:
                print(f"Game Over! The correct number was {number}.")
    except ValueError as e:
        print(f"Error: {e}. Please enter a valid number.")


# userGuess variable works correctly print(userGuess)
# test passed random number generates correctly and stores in a variable print(number)