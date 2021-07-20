"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

The program will execute the game 'Breakout'. Each player has 3 lives, the game will
stop when all the bricks are eliminated or no lives are remaining. Finally, the window
will show the final score and whether the player wins or loses the game.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second.
NUM_LIVES = 3


def main():
    """
    The program will execute the game 'Breakout'. Each player has 3 lives, the game will
    end when all the bricks are eliminated or no lives are remaining. Finally, the window
    will show the final score and whether the player wins or loses the game.
    """
    graphics = BreakoutGraphics()
    remaining = NUM_LIVES
    dx = graphics.get_x_velocity()
    dy = graphics.get_y_velocity()
    while True:
        pause(FRAME_RATE)
        if graphics.is_game_started:
            # If the ball bump into the left and the right margin of the window, the ball will bounce.
            if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window.width-graphics.ball.width:
                dx = -dx
            # If the ball bounce into the upper margin of the window, the ball will bounce.
            if graphics.ball.y <= 0:
                dy = -dy
            graphics.ball.move(dx, dy)
            # If probe_obj() returns true, the ball will has a opposite y-velocity.
            if graphics.probe_obj():
                dy = -dy
            # If the ball fall out the lower margin of the window, the variable 'remaining' will minus one.
            if graphics.ball.y >= graphics.window.height:
                remaining -= 1
                graphics.fall_out()
                dx = graphics.get_x_velocity()
                # If the variable 'remaining' bigger than 0, the game continues.
                if remaining > 0:
                    graphics.build_ball()
                    graphics.build_paddle()
                # However, if the variable 'remaining' smaller than 0, the game ends and the player loses.
                else:
                    graphics.game_over()
                    break
            # If the bricks are all eliminated, the game ends, but this time the player wins.
            if graphics.brick_left == 0:
                graphics.winner()
                break


if __name__ == '__main__':
    main()
