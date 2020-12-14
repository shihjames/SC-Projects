from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
Name: 
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    """
    Karel will first fill one street then go back to the
    starting point. After that, Karel will check whether it
    is on beeper then decide where to start to fill the
    next line.
    """
    while front_is_clear():
        fill_one_line()
        return_to_start()
        check_beeper()
    turn_left()
    while front_is_clear():
        fill_one_line()
    turn_around()
    # If the world is 1x1, Karel will put a beeper.
    if not front_is_clear():
        put_beeper()


def fill_one_line():
    """
    Pre-condition: Karel is at (1,1) and the world has no beeper.
    Post-condition: A certain street is filled by beepers in a spaced pattern,
    and Karel is at the East side of a certain street, facing East.
    """
    put_beeper()
    # Karel will first put a beeper before creating a spaced pattern.
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()


def return_to_start():
    """
    Pre-condition: A certain street is filled by beepers in a spaced pattern,
    and Karel is at the East side of a certain street, facing East.
    Post-condition: Karel has walked back to the West side of a certain street, facing North.
    """
    turn_around()
    # Turn to West
    while front_is_clear():
        move()
    turn_right()
    # Turn to North


def check_beeper():
    """
    Karel will decide how to work on the next street. If it is on a beeper, it will start filling
    the next street from the second avenue. Otherwise, it will still start filling form the first
    avenue.

    Pre-condition: Karel has walked back to the West side of a certain street, facing North.
    Post-condition1: If Karel is on beeper, it will walk to the second avenue of the next street.
    Post-condition2: If Karel is not on beeper, it will walk to the first avenue of the next street.
    """
    if on_beeper():
        if front_is_clear():
            move()
            turn_right()
            if front_is_clear():
                move()
    # Walk to the second avenue of the next street
    else:
        if front_is_clear():
            move()
            turn_right()
    # Walk to the first avenue of the next street.


def turn_around():
    """
    Karel will turn left twice.
    """
    turn_left()
    turn_left()


def turn_right():
    """
    Karel will turn left three times.
    """
    for i in range(3):
        turn_left()


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)