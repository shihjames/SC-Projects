"""
File: bouncing_ball.py
Name: James Shih
----------------------------------------
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
ball = GOval(15, 15, x=START_X, y=START_Y)
count = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    ball.fill_color = 'black'
    window.add(ball)
    onmouseclicked(bounce)


def bounce(_):
    """
    This function will be activate after a clicked by users, and the
    simulation of a bouncing ball starts. Users can only try three
    simulations and any click will not affect the process.
    """
    global ball, count
    # Only three tries are available
    if count < 3:
        # Click only works when the ball is at the starting point.
        if ball.x == START_X and ball.y == START_Y:
            # Set the velocity at perpendicular direction as zero.
            vy = 0
            while ball.x <= window.width:
                ball.move(VX, vy)
                vy += GRAVITY
                # When the ball reach the floor, the vertical speed is reversed.
                if ball.y >= window.height:
                    vy = -1 * REDUCE * vy
                pause(DELAY)
            # Count simulations
            count += 1
            # Reset the ball
            window.remove(ball)
            window.add(ball, START_X, START_Y)
    else:
        pass


if __name__ == "__main__":
    main()
