from karel.stanfordkarel import *

"""
File: MidpointKarel.py
Name: 
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    """
    Karel will put beeper to define border and keep narrowing down
    until it reach the midpoint of the street.
    """
    define_border()
    narrow_down()
    while not on_beeper():
        narrow_down1()
    pick_beeper()
    turn_around()
    check_front()
    if not on_beeper():
        put_beeper()


def define_border():
    """
    Karel will first put beeper on the leftmost margin of the street and
    walk to the rightmost margin, finally it will face west.
    """
    put_beeper()
    while front_is_clear():
        move()
    turn_around()


def narrow_down():
    """
    Karel will narrow down the first time by putting a beeper, then it will
    check whether the front is clear in order to decide what to do next.
    """
    if front_is_clear():
        move()
        if not on_beeper():
            put_beeper()
            check_front()
            # If front is clear, it will move on step.
        else:
            pass


def narrow_down1():
    """
    Karel will start narrow down for several times until it reach the mid point,
    and finally there will be only one beeper on the midpoint of the street.
    """
    while not on_beeper():
        move()
    pick_beeper()
    turn_around()
    if front_is_clear():
        move()
        put_beeper()
        check_front()


def check_front():
    """
    If front is clear, it will move on step.
    """
    if front_is_clear():
        move()


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
