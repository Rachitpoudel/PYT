import random
number = random.randint(1, 20)
guesses = []
for i in range(5):
    guess = int(input("Guess a number between 1 and 20: "))
    guesses.append(guess)
    if guess == number:
        print("Congratulations! You guessed the number!")
        break
    elif guess < number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")
if guess != number:
    print("Sorry, you ran out of guesses. The number was", number)
    print("Your guesses were:", guesses)
