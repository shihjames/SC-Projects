"""
File: fire.py
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    This function will scan through every pixel of the image and detects the pixels that are recognized as fire.
    Finally, the function will label them in red.
    :param filename: The directory of an image you want to process.
    :return: SimpleImage, parts of the image are labeled by red and other parts are in gray scale.
    """
    img = SimpleImage(filename)
    for pixel in img:
        avg = (pixel.red + pixel.green + pixel.blue) // 3
        # Highlight places that are on fire.
        if pixel.red > avg * HURDLE_FACTOR:
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        # Gray scale for other parts.
        else:
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    return img


def main():
    """
    The program will first show the original image, then execute function 'highlight_fires' to detects the
    pixels that are recognized as fire. Finally, it will show the processed image.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()
