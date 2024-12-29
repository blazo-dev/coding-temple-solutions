"""
👾💻 Guess the Secret: Number Challenge
Write a program where the user has to guess a secret number between 1 and 10.
The program provides feedback if the guess is too high or too low, and congratulates the user if they guess correctly.


HINT: Remember that random module we used a few lessons ago? It would be extremely helpful here... 

Steps:

Randomly select a secret number between 1-10. ✅
Ask the user to make a guess between 1-10.

If the user is correct, print "Congratulations, You guessed the secret number!"
If the user is too low, print "Too low!"
If the user is too high, print "Too high!"
"""

import random, time


print(
    """
   👾💻  Welcome to 'Guess the Secret Number Challenge'! 
------------------------------------------------------------
    I'm thinking of a secret number between 1 and 10. 
    Your goal is to guess the number!

    I'll tell you if your guess is too high or too low. 

    Good luck, and let's see if you can guess it right! 🎉
------------------------------------------------------------
"""
)

secret_number = random.randint(1, 10)

guess_number = int(input("Type a number between 1 and 10: "))
time.sleep(0.5)

while guess_number != secret_number:
    if guess_number < secret_number:
        print("Too low!")
    elif guess_number > secret_number:
        print("Too high!")

    guess_number = int(input("Try again! Type a number between 1 and 10: "))
    time.sleep(0.5)


print("Congratulations, You guessed the secret number!")
