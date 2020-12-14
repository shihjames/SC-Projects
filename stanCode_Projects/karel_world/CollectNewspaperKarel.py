from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
Name: 
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""


def main():
    """
    Karel will collect the newspaper then go back inside.
    """
    collect_newspaper()
    go_back_inside()


def collect_newspaper():
    """
    Pre-condition: Karel is facing East at the upper left corner of its house.
    Post-condition: Karel has just collected the newspaper, facing West.
    """
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()
    turn_around()


def go_back_inside():
    """
    Pre-condition: Karel has just collected the beeper, facing West.
    Post-condition: Karel and a beeper is at the upper left corner of the region, facing East.
    """
    for i in range(3):
        move()
    turn_right()
    move()
    turn_right()
    put_beeper()


def turn_right():
    """
    Karel will turn left three times.
    """
    for i in range(3):
        turn_left()


def turn_around():
    """
    Karel will turn left twice.
    """
    turn_left()
    turn_left()


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
