import random


def guesser(my_pick, your_guess, guess_counter=0):
    """

    :param my_pick: Random generated integer between 1-100
    :param your_guess: Integer from user to guess the picked number
    :param guess_counter: counts the number of guesses, default 0
    :return: A new integer that is asked to user if the guess is different from the picked number.
    """
    while True:
        guess_counter += 1
        if your_guess == my_pick:
            print(f"Congratulations! It took you {guess_counter} guesses to find it!")
            exit()
        elif your_guess > my_pick:
            your_guess = int(input("Go lower: "))
            guesser(my_pick, your_guess, guess_counter)
        elif your_guess < my_pick:
            your_guess = int(input("Go higher: "))
            guesser(my_pick, your_guess, guess_counter)
        return your_guess, guess_counter


def main():
    picked_number = random.randint(1, 101)
    guess = int(input("I have picked a number between 1 and 100. Make a guess: "))
    guesser(picked_number, guess)


main()
