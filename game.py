from random import randint
import sys

start = input("Would you like to play a little game?")


if start.lower() in ("yes", "y", "sure", "ok", "yeah", "yep", "of course", "why not", "let's go", "ye"):
    df = input("Alright! You'll be given three chances to randomely guess a number I am thinking of,"
      "between each (wrong) guess, You'll be given a change to get a hint."
      " You have three levels to choose from: Easy, Medium, and Hard."
      " Easy gives you a number between 1 and 10, Medium between 1 and 50, and Hard between 1 and 100."
        "Which level would you like to play on?").lower()
else:
    print("Thats alright, we'll see each other again.")
    sys.exit()


def number_generator(a, b):
    return randint(a, b)

def give_hint(number):
        hint_number = number
        while hint_number == number:
            hint_number = randint(max(1, number - 10,), number + 10)

        if hint_number < number:
            print(f"The number is higher than {hint_number}")
        elif hint_number > number:
            print(f"The number is lower than {hint_number}")



def game(number):
    attempts = 0
    no_of_hints = 0

    while attempts < 3: 
      guess = int(input("Please enter your guess:"))
      attempts +=1

      if guess == number:
        print("Congratulations! You guessed the number! And you used {} hints!".format(no_of_hints))
        sys.exit()
      else:
        print("Wrong guess.")
      if attempts < 3:
        want_hint = input("Would you like a hint? (y/n):")
        if want_hint.lower() == 'y':
            give_hint(number)
            no_of_hints +=1
      else:
             print("Sorry, you've used all your hints. The number was {}. Better luck next time!".format(number))
             sys.exit()

if df == "easy":
    number = number_generator(1, 10)
    game(number)
elif df == "medium":
    number = number_generator(1, 50)
    game(number)  
elif df == "hard":
    number = number_generator(1, 100)
    game(number)

