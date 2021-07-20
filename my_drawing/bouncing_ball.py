"""
File: bouncing_ball.py
Name: James Shih
-------------------------
This program simulates a bouncing ball at (START_X, START_Y)
that has VX as x velocity and 0 as y velocity. Each bounce reduces
y velocity to REDUCE of itself.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
count = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    window.add(ball)
    onmouseclicked(bounce)


def bounce(_):
    """
    This function will be activate after a clicked by users, and the
    simulation of a bouncing ball starts. Users can only try three
    simulations and any click will not affect the process.
    """
    global count
    # Only three tries are available
    if check(count):
        # Click only works when the ball is at the starting point.
        if ball.x == START_X and ball.y == START_Y:
            # Set the velocity at perpendicular direction as zero.
            vy = 0
            while True:
                ball.move(VX, vy)
                vy += GRAVITY
                # When the ball reach the floor, the vertical speed is reversed.
                if ball.y >= window.height:
                    vy *= -REDUCE
                pause(DELAY)
                # Count simulations
                if ball.x >= window.width:
                    window.remove(ball)
                    count += 1
                    break
            # Reset the ball
            window.add(ball, START_X, START_Y)


def check(n_bounce):
    if n_bounce < 3:
        return True


if __name__ == "__main__":
    main()
