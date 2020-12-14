from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
Name: 
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""


def main():
    """
    Karel will build all the columns needed.
    """
    while front_is_clear():
        check_beeper()
        build_up()
        walk_to_next_column()
    check_beeper()
    build_up()
    walk_down()


def check_beeper():
    """
    Check whether Karel is on a beeper or not, if not it will put a beeper.
    """
    if not on_beeper():
        put_beeper()


def build_up():
    """
    Pre-condition: Karel is at street 1, facing East.
    Post-condition: Karel is at the top of a column, facing North.
    """
    turn_left()
    for i in range(4):
        move()
        check_beeper()
        # Check whether Karel is on a beeper to avoid missing a beeper on the top (OBOB).


def turn_around():
    """
    Karel will turn left twice.
    """
    turn_left()
    turn_left()


def walk_to_next_column():
    """
    Pre-condition: Karel is at the top of a column, facing North.
    Post-condition: Karel is at street 1, facing East.
    """
    turn_around()
    for i in range(4):
        move()
    turn_left()
    for i in range(4):
        move()


def walk_down():
    """
    Pre-condition: Karel is at the top of the last column, facing North.
    Post-condition: Karel is at street 1, facing East.
    """
    turn_around()
    for i in range(4):
        move()
    turn_left()


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)