"""
File: sierpinski.py
Name: James Shih
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle.
LENGTH = 600               # The length of order 1 Sierpinski Triangle.
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle.
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle.
WINDOW_WIDTH = 950         # The width of the GWindow.
WINDOW_HEIGHT = 700        # The height of the GWindow.

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle.


def main():
	"""
	This program is a recursion algorithm aiming to draw a special triangle, the Sierpinski triangle.
	Given values of ORDER, LENGTH, UPPER_LEFT_X, and UPPER_LEFT_Y, the program will construct an
	n-order Sierpinski triangle.
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	This function recursively prints a certain order of Sierpinski triangle.
	:param order: Controls the order of Sierpinski triangle.
	:param length: Controls the length of Sierpinski triangle.
	:param upper_left_x: The x coordinate of the upper left vertex of a triangle.
	:param upper_left_y: The y coordinate of the upper left vertex of a triangle.
	"""
	pause(10)
	# Draw three line to create a triangle each time.
	line1 = GLine(upper_left_x, upper_left_y, upper_left_x+length, upper_left_y)
	line2 = GLine(upper_left_x, upper_left_y, upper_left_x+length*0.5, upper_left_y+length*0.866)
	line3 = GLine(upper_left_x+length, upper_left_y, upper_left_x+length*0.5, upper_left_y+length*0.866)
	# Add lines to window.
	window.add(line1)
	window.add(line2)
	window.add(line3)
	# Pass when order reduce to 1.
	if order == 1:
		return
	else:
		# Execute three recursion respectively.
		sierpinski_triangle(order-1, length*0.5, upper_left_x, upper_left_y)
		sierpinski_triangle(order-1, length*0.5, upper_left_x+length*0.5, upper_left_y)
		sierpinski_triangle(order-1, length*0.5, upper_left_x+length*0.25, upper_left_y+length*0.433)


if __name__ == '__main__':
	main()
