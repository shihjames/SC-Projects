"""
File: blur.py
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    This function uses average RGB values to blur an image. It automatically chooses
    neighbors of each pixels and replaces their RGB values to their neighbors' average
    RGB values.
    :param img: SimpleImage, the original image you want to blur.
    :return: SimpleImage, blurred image.
    """
    img_blank = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            new_pixel = img_blank.get_pixel(x, y)
            # Left upper corner.
            if x == 0 and y == 0:
                new_pixel.red = (img.get_pixel(x, y + 1).red + img.get_pixel(x + 1, y).red + img.get_pixel(x + 1, y + 1).red + img.get_pixel(x, y).red) // 4
                new_pixel.green = (img.get_pixel(x, y + 1).green + img.get_pixel(x + 1, y).green + img.get_pixel(x + 1, y + 1).green + img.get_pixel(x, y).green) // 4
                new_pixel.blue = (img.get_pixel(x, y + 1).blue + img.get_pixel(x + 1, y).blue + img.get_pixel(x + 1, y + 1).blue) + img.get_pixel(x, y).blue // 4
            # Left side
            elif x == 0 and y != 0 and y != img.height - 1:
                new_pixel.red = (img.get_pixel(x, y - 1).red + img.get_pixel(x, y + 1).red + img.get_pixel(x + 1, y - 1).red + img.get_pixel(x + 1, y).red + img.get_pixel(x + 1, y + 1).red + img.get_pixel(x, y).red) // 6
                new_pixel.green = (img.get_pixel(x, y - 1).green + img.get_pixel(x, y + 1).green + img.get_pixel(x + 1, y - 1).green + img.get_pixel(x + 1, y).green + img.get_pixel(x + 1, y + 1).green + img.get_pixel(x, y).green) // 6
                new_pixel.blue = (img.get_pixel(x, y - 1).blue + img.get_pixel(x, y + 1).blue + img.get_pixel(x + 1, y - 1).blue + img.get_pixel(x + 1, y).blue + img.get_pixel(x + 1, y + 1).blue + img.get_pixel(x, y).blue) // 6
            # Left lower corner
            elif x == 0 and y == img.height - 1:
                new_pixel.red_ = (img.get_pixel(x, img.height - 1 - 1).red + img.get_pixel(x + 1, img.height - 1).red + img.get_pixel(x + 1, img.height - 1 - 1).red + img.get_pixel(x, y).red) // 4
                new_pixel.green = (img.get_pixel(x, img.height - 1 - 1).green + img.get_pixel(x + 1, img.height - 1).green + img.get_pixel(x + 1, img.height - 1 - 1).green + img.get_pixel(x, y).green) // 4
                new_pixel.blue = (img.get_pixel(x, img.height - 1 - 1).blue + img.get_pixel(x + 1, img.height - 1).blue + img.get_pixel(x + 1, img.height - 1 - 1).blue + img.get_pixel(x, y).blue) // 4
            # Top.
            elif y == 0 and x != 0 and x != img.width - 1:
                new_pixel.red = (img.get_pixel(x - 1, y).red + img.get_pixel(x + 1, y).red + img.get_pixel(x - 1, y + 1).red + img.get_pixel(x, y + 1).red + img.get_pixel(x + 1, y + 1).red + img.get_pixel(x, y).red) // 6
                new_pixel.green = (img.get_pixel(x - 1, y).green + img.get_pixel(x + 1, y).green + img.get_pixel(x - 1, y + 1).green + img.get_pixel(x, y + 1).green + img.get_pixel(x + 1, y + 1).green + img.get_pixel(x, y).green) // 6
                new_pixel.blue = (img.get_pixel(x - 1, y).blue + img.get_pixel(x + 1, y).blue + img.get_pixel(x - 1, y + 1).blue + img.get_pixel(x, y + 1).blue + img.get_pixel(x + 1, y + 1).blue + img.get_pixel(x, y).blue) // 6
            # Pixels not on the corners or sides.
            elif x != 0 and x != img.width - 1 and y != 0 and y != img.height - 1:
                new_pixel.red = (img.get_pixel(x - 1, y - 1).red + img.get_pixel(x - 1, y).red + img.get_pixel(x - 1, y + 1).red + img.get_pixel(x, y - 1).red + img.get_pixel(x, y + 1).red + img.get_pixel(x + 1, y - 1).red + img.get_pixel(x + 1, y).red + img.get_pixel(x + 1, y + 1).red + img.get_pixel(x, y).red) // 9
                new_pixel.green = (img.get_pixel(x - 1, y - 1).green + img.get_pixel(x - 1, y).green + img.get_pixel(x - 1, y + 1).green + img.get_pixel(x, y - 1).green + img.get_pixel(x, y + 1).green + img.get_pixel(x + 1, y - 1).green + img.get_pixel(x + 1, y).green + img.get_pixel(x + 1, y + 1).green + img.get_pixel(x, y).green) // 9
                new_pixel.blue = (img.get_pixel(x - 1, y - 1).blue + img.get_pixel(x - 1, y).blue + img.get_pixel(x - 1, y + 1).blue + img.get_pixel(x, y - 1).blue + img.get_pixel(x, y + 1).blue + img.get_pixel(x + 1, y - 1).blue + img.get_pixel(x + 1, y).blue + img.get_pixel(x + 1, y + 1).blue + img.get_pixel(x, y).blue) // 9
            # Bottom
            elif y == img.height - 1 and x != 0 and x != img.width - 1:
                new_pixel.red = (img.get_pixel(x - 1, y).red + img.get_pixel(x - 1, y - 1).red + img.get_pixel(x, y - 1).red + img.get_pixel(x + 1, y - 1).red + img.get_pixel(x + 1, y).red + img.get_pixel(x, y).red) // 6
                new_pixel.green = (img.get_pixel(x - 1, y).green + img.get_pixel(x - 1, y - 1).green + img.get_pixel(x, y - 1).green + img.get_pixel(x + 1, y - 1).green + img.get_pixel(x + 1, y).green + img.get_pixel(x, y).green) // 6
                new_pixel.blue = (img.get_pixel(x - 1, y).blue + img.get_pixel(x - 1, y - 1).blue + img.get_pixel(x, y - 1).blue + img.get_pixel(x + 1, y - 1).blue + img.get_pixel(x + 1, y).blue + img.get_pixel(x, y).blue) // 6
            # Right upper corner.
            elif x == img.width - 1 and y == 0:
                new_pixel.red_ = (img.get_pixel(img.width - 2, y).red + img.get_pixel(img.width - 2, y + 1).red + img.get_pixel(img.width - 1, y + 1).red + img.get_pixel(x, y).red) // 4
                new_pixel.green = (img.get_pixel(img.width - 2, y).green + img.get_pixel(img.width - 2, y + 1).green + img.get_pixel(img.width - 1, y + 1).green + img.get_pixel(x, y).green) // 4
                new_pixel.blue = (img.get_pixel(img.width - 2, y).blue + img.get_pixel(img.width - 2, y + 1).blue + img.get_pixel(img.width - 1, y + 1).blue + img.get_pixel(x, y).blue) // 4
            # Right side.
            elif x == img.width - 1 and y != 0 and y != img.height - 1:
                new_pixel.red = (img.get_pixel(x, y - 1).red + img.get_pixel(x - 1, y - 1).red + img.get_pixel(x - 1, y).red + img.get_pixel(x - 1, y + 1).red + img.get_pixel(x, y + 1).red + img.get_pixel(x, y).red) // 6
                new_pixel.green = (img.get_pixel(x, y - 1).green + img.get_pixel(x - 1, y - 1).green + img.get_pixel(x - 1, y).green + img.get_pixel(x - 1, y + 1).green + img.get_pixel(x, y + 1).green + img.get_pixel(x, y).green) // 6
                new_pixel.blue = (img.get_pixel(x, y - 1).blue + img.get_pixel(x - 1, y - 1).blue + img.get_pixel(x - 1, y).blue + img.get_pixel(x - 1, y + 1).blue + img.get_pixel(x, y + 1).blue + img.get_pixel(x, y).blue) // 6
            # Right lower corner.
            elif x == img.width - 1 and y == img.height - 1:
                new_pixel.red__ = (img.get_pixel(img.width - 2, img.height - 1).red + img.get_pixel(img.width - 2, img.height - 2).red + img.get_pixel(img.width - 1, img.height - 2).red + img.get_pixel(x, y).red) // 4
                new_pixel.green = (img.get_pixel(img.width - 2, img.height - 1).green + img.get_pixel(img.width - 2, img.height - 2).green + img.get_pixel(img.width - 1, img.height - 2).green + img.get_pixel(x, y).green) // 4
                new_pixel.blue = (img.get_pixel(img.width - 2, img.height - 1).blue + img.get_pixel(img.width - 2, img.height - 2).blue + img.get_pixel(img.width - 1, img.height - 2).blue + img.get_pixel(x, y).blue) // 4

    return img_blank


def main():
    """
    The program will first show the original image then execute the function 'blur' to blur the image.
    Finally, it will show the blurred image.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()
    blurred_img = blur(old_img)
    for i in range(9):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
