"""
File: shrink.py
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    The function will make the original image shrink to its half without losing too much quality.
    :param filename: The directory of an image tou want to process.
    :return img: SimpleImage, a shrink image that is similar to the original image.
    """
    img = SimpleImage(filename)
    # Create a blank image that its size is 1/2 of the original image.
    img_blank = SimpleImage.blank(img.width // 2, img.height // 2)
    for x in range(img_blank.width):
        for y in range(img_blank.height):
            new_pixel = img_blank.get_pixel(x, y)
            # Right upper corner.
            if x == 0 and y == 0:
                new_pixel.red = (img.get_pixel(x, y+1).red + img.get_pixel(x+1, y).red + img.get_pixel(x+1, y+1).red + img.get_pixel(x, y).red) // 4
                new_pixel.green = (img.get_pixel(x, y+1).green + img.get_pixel(x+1, y).green + img.get_pixel(x+1, y+1).green + img.get_pixel(x, y).green) // 4
                new_pixel.blue = (img.get_pixel(x, y+1).blue + img.get_pixel(x+1, y).blue + img.get_pixel(x+1, y+1).blue) + img.get_pixel(x, y).blue // 4
            # Left side.
            elif x == 0 and y != 0:
                new_pixel.red = (img.get_pixel(x, y*2).red + img.get_pixel(x, y*2+1).red + img.get_pixel(x+1, y*2).red + img.get_pixel(x+1, y*2+1).red) // 4
                new_pixel.green = (img.get_pixel(x, y*2).green + img.get_pixel(x, y*2+1).green + img.get_pixel(x+1, y*2).green + img.get_pixel(x+1, y*2+1).green) // 4
                new_pixel.blue = (img.get_pixel(x, y*2).blue + img.get_pixel(x, y*2+1).blue + img.get_pixel(x+1, y*2).blue + img.get_pixel(x+1, y*2+1).blue) // 4
            # Top.
            elif y == 0 and x != 0:
                new_pixel.red = (img.get_pixel(x*2, y).red + img.get_pixel(x*2+1, y).red + img.get_pixel(x*2, y+1).red + img.get_pixel(x*2+1, y+1).red) // 4
                new_pixel.green = (img.get_pixel(x*2, y).green + img.get_pixel(x*2+1, y).green + img.get_pixel(x*2, y+1).green + img.get_pixel(x*2+1, y+1).green) // 4
                new_pixel.blue = (img.get_pixel(x*2, y).blue + img.get_pixel(x*2+1, y).blue + img.get_pixel(x*2, y+1).blue + img.get_pixel(x*2+1, y+1).blue) // 4
            else:
                new_pixel.red = (img.get_pixel(x*2, y*2).red + img.get_pixel(x*2+1, y*2).red + img.get_pixel(x*2, y*2+1).red + img.get_pixel(x*2+1, y*2+1).red) // 4
                new_pixel.green = (img.get_pixel(x*2, y*2).green + img.get_pixel(x*2+1, y*2).green + img.get_pixel(x*2, y*2+1).green + img.get_pixel(x*2+1, y*2+1).green) // 4
                new_pixel.blue = (img.get_pixel(x*2, y*2).blue + img.get_pixel(x*2+1, y*2).blue + img.get_pixel(x*2, y*2+1).blue + img.get_pixel(x*2+1, y*2+1).blue) // 4
    return img_blank


def main():
    """
    The program will first show the original image then execute function 'shrink'. Finally, it will show a shrink image.
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
