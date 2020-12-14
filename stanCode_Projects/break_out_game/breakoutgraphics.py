"""
File: breakoutgraphics.py
Name: James Shih
----------------------------------------
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).
INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):
        """
        Parameter settings.
        :param ball_radius: Controls the radius of the ball.
        :param paddle_width: Controls the width of the paddle.
        :param paddle_height: Controls the height of the paddle.
        :param paddle_offset: Controls the y-position of the paddle.
        :param brick_rows: Controls the number of rows of bricks.
        :param brick_cols: Controls the number of columns of bricks.
        :param brick_width: Controls the width of a single brick.
        :param brick_height: Controls the height of a single brick.
        :param brick_offset: Controls the y-position of the highest row of bricks.
        :param brick_spacing: Controls the interval between any two bricks.
        :param title: Set the title of the canvas.
        """
        self.ball_radius = ball_radius
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height
        self.paddle_offset = paddle_offset
        self.brick_cols = brick_cols
        self.brick_rows = brick_rows
        self.brick_width = brick_width
        self.brick_height = brick_height
        self.brick_offset = brick_offset
        self.brick_spacing = brick_spacing

        # Create a label for usernames before create a window.
        self.name = GLabel('Player: ' + input('Nickname: '))
        self.name.font = '-15-bold'

        # Create a graphical window, with some extra space.
        self.window_width = self.brick_cols * (brick_width+brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height+brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Initial settings before the game starts.
        self.score = 0
        self.score_label = GLabel('Score: ' + str(self.score))
        self.score_label.font = '-15-bold'
        self.lives = 3
        self.lives_label = GLabel('Lives: ' + str(self.lives))
        self.lives_label.font = '-15-bold'
        self.click2start = GLabel('Click to Start !')
        self.click2start.font = '-20-bold'
        self.window.add(self.name, 5, self.brick_offset - 25)
        self.window.add(self.click2start, 130, self.window.height-150)
        self.window.add(self.score_label, 5, self.window.height)
        self.window.add(self.lives_label, self.window_width-100, self.window_height-5)

        # Create a paddle.
        self.count = 1  # For paddle width resetting after losing one live.
        self.paddle = GRect(self.paddle_width, self.paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window_width-self.paddle_width)/2, y=self.window_height-paddle_offset)

        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, (self.window_width-self.ball.width)/2, (self.window_height-brick_height)/2)

        # Default initial velocity for the ball.
        self.__dx = 0
        self.__dy = INITIAL_Y_SPEED
        self.set_x_velocity()

        # Initialize our mouse listeners.
        self.is_game_started = False
        onmouseclicked(self.handle_click)

        # Draw bricks.
        self.brick_left = self.brick_cols * self.brick_rows
        for i in range(self.brick_rows):
            for j in range(self.brick_cols):
                # Different colors for every two rows.
                self.brick = GRect(self.brick_width, self.brick_height)
                self.brick.filled = True
                if i < 2:
                    self.brick.fill_color = 'lightcoral'
                elif 2 <= i < 4:
                    self.brick.fill_color = 'peachpuff'
                elif 4 <= i < 6:
                    self.brick.fill_color = 'lightyellow'
                elif 6 <= i < 8:
                    self.brick.fill_color = 'palegreen'
                elif 8 <= i < 10:
                    self.brick.fill_color = 'aqua'
                self.window.add(self.brick, x=j*(self.brick_width+self.brick_spacing),
                                y=self.brick_offset+i*(self.brick_height+self.brick_spacing))

    def paddle_move(self, event):
        """
        This function will execute if the the game is started. If the game is started,
        it will detect the position of the mouse so that players can control the paddle
        with their mouse.
        :param event: Detects position of the mouse.
        """
        if self.is_game_started:
            # If the mouse is out of the range of the width of the window, the paddle will still remain in the window.
            if event.x <= self.paddle.width/2:
                self.paddle.x = 0
            elif event.x >= self.window.width - self.paddle.width/2:
                self.paddle.x = self.window.width - self.paddle.width
            else:
                self.paddle.x = event.x - self.paddle.width/2

    def get_x_velocity(self):
        """
        Since self.__dx is private instance variable, we need to create a getter for the user-end.
        :return: The value of self.__dx (the x-velocity)
        """
        return self.__dx

    def get_y_velocity(self):
        """
        Since self.__dy is private instance variable, we need to create a getter for the user-end.
        :return: The value of self.__dy (the y-velocity)
        """
        return self.__dy

    def set_x_velocity(self):
        """
        Setting a random x-velocity and y-velocity for the ball. The y-velocity is a constant, and
        the x-velocity is set between 1 and MAX_X_SPEED, There is a 50% chance that the ball will have
        opposite direction in x dimension.
        """
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() < 0.5:
            self.__dx = -self.__dx

    def handle_click(self, event):
        """
        This function will execute if a click on the mouse. After a single click,
        the game will start, and any clicks can no longer affect the game.
        :param event: Detects a click on the mouse.
        :return: self.count
        """
        self.window.remove(self.click2start)
        self.is_game_started = True
        onmousemoved(self.paddle_move)

    def probe_obj(self):
        """
        This function will detect any collision between the ball with other objects.
        :return: True, if the ball bump into the paddle or the bricks.
        """
        # The variable 'obj' will change to the next corner if the checked None.
        obj = self.window.get_object_at(self.ball.x, self.ball.y)
        if obj is None or obj is self.name and obj is self.score_label and obj is self.lives_label:
            obj = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y)
        if obj is None or obj is self.name and obj is self.score_label and obj is self.lives_label:
            obj = self.window.get_object_at(self.ball.x, self.ball.y+self.ball.height)
        if obj is None or obj is self.name and obj is self.score_label and obj is self.lives_label:
            obj = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y+self.ball.height)
        if obj is self.paddle:
            # To avoid the ball from sticking on the paddle, I move the ball above the paddle.
            self.ball.move(0, -self.paddle_height - self.ball.height)
            # When the ball touches the paddle, the paddle will change its color to the ball's color.
            self.paddle.color = self.ball.color
            self.paddle.fill_color = self.ball.fill_color
            return True
        elif obj is not self.paddle and obj is not None and obj is not self.name and obj is not self.score_label \
                and obj is not self.lives_label:
            # Every time when the ball bump into a brick, the score will reset.
            self.window.remove(obj)
            self.brick_left -= 1
            # The formula of score counting.
            self.score = int((self.brick_rows * self.brick_cols - self.brick_left) ** 1.5)
            if self.brick_left == (self.brick_rows * self.brick_cols) * 1/2:
                self.lives += 1
                self.window.remove(self.lives_label)
                self.lives_label = GLabel('Lives: ' + str(self.lives))
                self.lives_label.font = '-15-bold'
                self.window.add(self.lives_label, self.window_width-100, self.window_height-5)
            self.window.remove(self.score_label)
            self.score_label = GLabel('Score: ' + str(self.score))
            self.score_label.font = '-15-bold'
            self.window.add(self.score_label, 5, self.window.height)
            # The color of the ball depends on how many bricks are left.
            if self.brick_rows * self.brick_cols * 3/5 < self.brick_left <= self.brick_rows * self.brick_cols * 4/5:
                self.ball.color = 'palegreen'
                self.ball.fill_color = 'palegreen'
            elif self.brick_rows * self.brick_cols * 2/5 < self.brick_left <= self.brick_rows * self.brick_cols * 3/5:
                self.ball.color = 'lightyellow'
                self.ball.fill_color = 'lightyellow'
            elif self.brick_rows * self.brick_cols * 1/5 < self.brick_left <= self.brick_rows * self.brick_cols * 2/5:
                self.ball.color = 'peachpuff'
                self.ball.fill_color = 'peachpuff'
            # More difficult to see the ball.
            elif self.brick_left <= self.brick_rows * self.brick_cols * 1/5:
                self.ball.color = 'black'
                self.ball.fill_color = 'black'
            return True
        # Lives will reset when the ball fall out of the lower margin of the window.

    def fall_out(self):
        self.is_game_started = False
        # Every chance loses, the variable 'count', which affects the length of the paddle, will add 0.15.
        self.count += 0.15
        self.lives -= 1
        self.window.remove(self.lives_label)
        self.lives_label = GLabel('Lives: ' + str(self.lives))
        self.lives_label.font = '-15-bold'
        self.window.add(self.lives_label, self.window_width - 100, self.window_height - 5)
        self.set_x_velocity()
        return self.count, self.lives, self.__dx

    def build_ball(self):
        """
        This function will first remove the original ball and create a new ball. The color of the ball depends
        on the number of remaining bricks.
        """
        self.window.remove(self.ball)
        self.ball = GOval(self.ball_radius*2, self.ball_radius*2)
        self.ball.filled = True
        # The color of the ball depends on how many bricks are left.
        if self.brick_rows * self.brick_cols * 3 / 5 < self.brick_left <= self.brick_rows * self.brick_cols * 4 / 5:
            self.ball.color = 'palegreen'
            self.ball.fill_color = 'palegreen'
        elif self.brick_rows * self.brick_cols * 2 / 5 < self.brick_left <= self.brick_rows * self.brick_cols * 3 / 5:
            self.ball.color = 'lightyellow'
            self.ball.fill_color = 'lightyellow'
        elif self.brick_rows * self.brick_cols * 1 / 5 < self.brick_left <= self.brick_rows * self.brick_cols * 2 / 5:
            self.ball.color = 'peachpuff'
            self.ball.fill_color = 'peachpuff'
        # More difficult to see the ball.
        elif self.brick_left <= self.brick_rows * self.brick_cols * 1 / 5:
            self.ball.color = 'black'
            self.ball.fill_color = 'black'
        self.window.add(self.ball, (self.window_width-self.ball.width)/2, (self.window_height-self.brick_height)/2)

    def build_paddle(self):
        """
        This function will first remove the original paddle and create a new one. The width of the new paddle
        depends on the variable of count.
        """
        self.window.remove(self.paddle)
        self.paddle = GRect(self.paddle_width/self.count, self.paddle_height, x=(self.window_width-self.paddle_width)/2,
                            y=self.window_height-self.paddle_offset)
        self.paddle.filled = True
        self.paddle.color = self.ball.color
        self.paddle.fill_color = self.ball.fill_color
        self.window.add(self.paddle)

    def game_over(self):
        """
        This function execute when no lives are remaining. The window will show the game is over
        and the final score. The score depends on the number of remaining bricks and the variable
        count.
        """
        self.is_game_started = False
        self.window.clear()
        game_over = GLabel('Game Over')
        game_over.font = '-60-bold'
        lose = GLabel('You Lose...')
        lose.font = '-30-bold'
        score_label = GLabel('Your Score:' + str(self.score))
        score_label.font = 'courier-25-bold'
        background = GRect(self.window.width, self.window.height)
        background.filled = True
        background.color = 'red'
        background.fill_color = 'red'
        self.window.add(background)
        self.window.add(game_over, 2, (self.window.height/2)+30)
        self.window.add(lose, 120, (self.window.height/2+120))
        self.window.add(score_label, 100, self.window.height)

    def winner(self):
        """
        This function will execute if and only if a player successfully eliminates
        all the bricks. After all bricks are eliminated, the window will show
        'You win!!!!' and the final score. The score depends on the number of remaining
        bricks and the variable count.
        """
        self.window.clear()
        you_win = GLabel('Love Cindy!!!!')
        you_win.font = '-60-bold'
        # One live remaining worth 100 points.
        self.score += self.lives * 100
        score_label = GLabel('Your Score is:' + str(self.score), 0, 20)
        score_label.font = 'courier-25-bold'
        background = GRect(self.window.width, self.window.height)
        background.filled = True
        background.color = 'pink'
        background.fill_color = 'pink'
        self.window.add(background)
        self.window.add(you_win, 5, (self.window.height/2)+30)
        self.window.add(score_label, 50, self.window.height)
