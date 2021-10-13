import random

randomNumber = random.randint(1, 20)
guessCount = 0
print("I am thinking of a number between 1 and 20.")

for i in range(1,10):
    guess = int(input("Take a guess: "))
    guessCount = i
    if guess < randomNumber:
        print("Your guess is too low ")

    elif guess > randomNumber:
        print("Your guess is too high ")

    elif guess == randomNumber:
        break

if guess == randomNumber:
    print("Good job, you guessed my number in " + str(guessCount) + " guesses")
else:
    print("You Lose!! The number was " + str(randomNumber))