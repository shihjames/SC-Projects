"""
File: babygraphics.py
Name: James Shih
----------------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter as tk
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000  # Controls the width of the canvas.
CANVAS_HEIGHT = 600  # Controls the height of the canvas.
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]  # List of years.
GRAPH_MARGIN_SIZE = 20  # Controls the margin size.
COLORS = ['red', 'orange', 'green', 'blue', 'purple']  # List of colors.
TEXT_DX = 2  # Controls the position of a text.
LINE_WIDTH = 2  # Controls the width of a line.
MAX_RANK = 1000  # The maximum ranking.


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    # Variable rang defines the range we can draw lines.
    rang = width - 2 * GRAPH_MARGIN_SIZE
    #  The interval of x is rang/len(YEARS)
    x_coordinate = GRAPH_MARGIN_SIZE + (rang / len(YEARS)) * year_index
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    # delete all existing lines from the canvas
    canvas.delete('all')
    # Create upper and lower margin line
    canvas.create_line(0, GRAPH_MARGIN_SIZE, CANVAS_WIDTH, GRAPH_MARGIN_SIZE)
    canvas.create_line(0, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    # Draw line and text for every year.
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        canvas.create_text(x+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tk.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    # Draw the fixed background grid.
    draw_fixed_lines(canvas)
    # Loop over every name in lookup_names.
    for i in range(len(lookup_names)):
        name = lookup_names[i]
        if str(YEARS[0]) in name_data[name]:
            rank = name_data[name][str(YEARS[0])]
        # If year doesn't exist in a certain name, assign rank to '*'.
        else:
            rank = '*'
        # (prev_x, prev_y) is the position representing the ranking in the previous year of a certain name.
        prev_x = get_x_coordinate(CANVAS_WIDTH, 0)
        prev_y = get_y_coordinate(rank)
        canvas.create_text(prev_x, prev_y, text=name+' '+rank, anchor=tk.SW, fill=COLORS[i])
        for j in range(1, len(YEARS)):
            # Variable x is the x_coordinate of the position of the next year.
            x = get_x_coordinate(CANVAS_WIDTH, j)
            if str(YEARS[j]) in name_data[name]:
                rank = name_data[name][str(YEARS[j])]
            # If year doesn't exist in a certain name, assign rank to '*'.
            else:
                rank = '*'
            y = get_y_coordinate(rank)
            # Draw line and text to show the rise or fall in ranking of a certain name.
            canvas.create_line(prev_x, prev_y, x, y, width=LINE_WIDTH, fill=COLORS[i])
            canvas.create_text(x, y, text=name+' '+rank, anchor=tk.SW, fill=COLORS[i])
            # Reassign prev_x and prev_y to x and y
            prev_x = x
            prev_y = y


def get_y_coordinate(rank):
    """
    Given the rank, returns the y_coordinate of the position.
    :param rank : str, the ranking of a certain name.
    :return: int, the y_coordinate of the position.
    """
    unit_h = (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / MAX_RANK
    if rank == '*':
        y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
    else:
        y = GRAPH_MARGIN_SIZE + unit_h * int(rank)
    return y


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tk.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
