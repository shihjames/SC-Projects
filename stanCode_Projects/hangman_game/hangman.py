"""
File: hangman.py
Name: James Shih
----------------------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program will randomly pick one word and the player need to guess
    what exactly the word is in certain tries. In each turn, the player
    need to input one letter, then the program will tell whether the
    letter is in the word. If the player find out what the word is in N_TURNS
    tries, the player wins. However, if the player couldn't find out the word
    in N_TURNS, the player loses.
    """
    n_guesses = 0
    # Assign ans to a randomly picked word.
    ans = random_word()
    print('The word looks like:', end=' ')
    # Variable 'show' shows the progress of guessing
    show = '-' * len(ans)
    print(show)
    print('You have ' + str(N_TURNS - n_guesses) + ' guesses left.')
    hang_man(n_guesses, ans, show)


def hang_man(n_guesses, ans, show):
    """
    This function is the main body of the game 'hangman'
    """
    while n_guesses < N_TURNS:
        guess = input('Your guess: ').upper()
        # Check input is an alphabet.
        if not guess.isalpha():
            print('Illegal format')
        # Check input is a single letter.
        elif len(guess) > 1:
            print('Illegal format')
        else:
            correct = ''
            if guess not in ans:
                n_guesses += 1
                print('There is no ' + str(guess) + " 's in the word")
                print('The word looks like:', end=' ')
                print(show)
                print('You have ' + str(N_TURNS-n_guesses) + ' guesses left.')
                build_hangman(n_guesses)
            else:
                for i in range(len(ans)):
                    if ans[i] == guess:
                        correct += ans[i]
                    else:
                        correct += show[i]
                show = correct
                print('The word looks like:', end=' ')
                print(correct)
                print('You are correct!')
        if show.isalpha():
            print('You win!!')
            print('The word is: ' + ans)
            n_guesses = 100
    if n_guesses == 7:
        print('You are completely hung ：( ')
        print('The word is: ' + ans)


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


def build_hangman(n_guesses):
    """
    This function will gradually show hangman as n_guesses increase until hangman is completely hung.
    """
    if n_guesses == 1:
        print('_____')
        print('|   |')
        print('|   (')
        print('|')
        print('|')
        print('|')
    if n_guesses == 2:
        print('_____')
        print('|   |')
        print('|   o')
        print('|')
        print('|')
        print('|')
    if n_guesses == 3:
        print('_____')
        print('|   |')
        print('|   o')
        print('|   |')
        print('|')
        print('|')
    if n_guesses == 4:
        print('_____')
        print('|   |')
        print('|   o')
        print('|  \\|')
        print('|')
        print('|')
    if n_guesses == 5:
        print('_____')
        print('|   |')
        print('|   o')
        print('|  \\|/')
        print('|')
        print('|')
    if n_guesses == 6:
        print('_____')
        print('|   |')
        print('|   o')
        print('|  \\|/')
        print('|  /')
        print('|')
    if n_guesses == 7:
        print('_____')
        print('|   |')
        print('|   o')
        print('|  \\|/')
        print('|  / \\')
        print('| You Dead!!!')


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
