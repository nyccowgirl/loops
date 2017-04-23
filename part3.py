from random import randint


def guess_num():
    """Uses a while loop to prompt user to guess a secret number between 1 and 10."""

random_integer = randint(1, 10)

while True:
    guess = raw_input("Guess the secret number between 1 and 10: ")
    if not guess.isdigit():
        print "Please guess an integer."
    else:
        guess = int(guess)
        if (guess < 1) or (guess > 10):
            print "Number out of range."
        else:
            if guess < random_integer:
                print "That guess is too low."
            elif guess > random_integer:
                print "That guess is too high."
            elif guess == random_integer:
                print "Bueno! You guessed correctly!"
                break