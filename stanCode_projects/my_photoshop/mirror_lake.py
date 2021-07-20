"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    This function will flip an image, making it looks like a reflected image.
    :param filename: The directory of an image you want to process.
    :return: SimpleImage, a perpendicularly flipped image.
    """
    img_mirror = SimpleImage(filename)
    # Create a blank image which is 2 times higher than the original image.
    img_blank = SimpleImage.blank(img_mirror.width, img_mirror.height*2)
    for x in range(img_mirror.width):
        for y in range(img_mirror.height):
            old_pixel = img_mirror.get_pixel(x, y)
            new_pixel1 = img_blank.get_pixel(x, y)
            # Variable new_pixel2 represents pixels in the lower part of the blank image.
            new_pixel2 = img_blank.get_pixel(x, img_blank.height-y-1)
            new_pixel1.red = old_pixel.red
            new_pixel1.green = old_pixel.green
            new_pixel1.blue = old_pixel.blue
            new_pixel2.red = old_pixel.red
            new_pixel2.green = old_pixel.green
            new_pixel2.blue = old_pixel.blue
    return img_blank


def main():
    """
    The program will first show the original image, then execute the function 'reflect' to
    perpendicularly flip the original image, making it looks like a reflected image. Finally,
    it will show the processed image.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
