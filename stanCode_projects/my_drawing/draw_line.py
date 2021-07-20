"""
File: draw_line.py
Name: James Shih
-------------------------
This program creates lines on an instance of GWindow class.
There is a circle indicating the user’s first click. A line appears
at the condition where the circle disappears as the user clicks
on the canvas for the second time.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# Constant controls dot size
SIZE = 10

# Global variables
window = GWindow()
dot = GOval(SIZE, SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_dot)


def draw_dot(event):
    # Draw the first dot at the point clicked.
    global dot
    dot.move(event.x-dot.x-dot.width/2, event.y-dot.y-dot.height/2)
    window.add(dot)
    # The next click will activate the function: form_line.
    onmouseclicked(form_line)


def form_line(e):
    # Form a line from the dot to the coordinate clicked.
    path = GLine(dot.x+SIZE/2, dot.y+SIZE/2, e.x, e.y)
    window.add(path)
    # The dot will be removed when the line is formed.
    window.remove(dot)
    onmouseclicked(draw_dot)


if __name__ == "__main__":
    main()
