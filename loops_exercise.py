"""
This file should be used to complete Parts 2 and 3 in the Hackbright Prep loops
exercise. Part 1 may be completed in the Python interpreter.
"""

#####################################################################
# PART 2: For Loops


def print_1_to_10():
    """Prints out numbers from 1 to 10, not including 10.

    >>> print_1_to_10()
    1
    2
    3
    4
    5
    6
    7
    8
    9
    """
    for number in range(1, 10):
        print number
    pass


def print_10_to_15():
    """Prints out numbers from 10 to 15, exclusive, but prints 'hello' if the number is 13.

    >>> print_10_to_15()
    10
    11
    12
    hello
    14
    """
    for number in range(10, 15):
        if number == 13:
            print "hello"
        else:
            print number
    pass


def print_list_v1(fruits):
    """Prints out each item in a list, without using the range function.

    >>> fruits = ['apple', 'berry', 'cherry']
    >>> print_list_v1(fruits)
    apple
    berry
    cherry
    """
    for item in fruits:
        print item
    pass


def print_list_v2(fruits):
    """Prints out each item in a list, using the range function.

    >>> fruits = ['apple', 'berry', 'cherry']
    >>> print_list_v2(fruits)
    apple
    berry
    cherry
    """
    for var in range(len(fruits)):
        print fruits[var]
    pass


def sum_nums(num):
    """Add up all numbers from 0 to num, not inclusive, and prints the sum.

    Solve this without using Python's built-in sum() function.

    >>> sum_nums(8)
    28
    """
    total = 0
    for num in range(num):
        total += num
    print total
    pass


#####################################################################
# PART 3: While Loops

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
    pass


#####################################################################
# Don't touch the code below!
# This is just allowing us to run the doctests

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"