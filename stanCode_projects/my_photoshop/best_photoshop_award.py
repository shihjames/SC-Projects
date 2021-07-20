"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage
THRESHOLD = 1.3
BLACK_PIXEL = 160


def main():
    """
    This function conducts green screen replacement
    which is able to photoshop a person onto any background
    Idea: My dream is to live in LA and enjoy the culture. I love
    Hollywood movies so I will absolutely visit the 'Hollywood
    sign' in the future. This combined image is my imagination of
    the future.
    """
    img = SimpleImage('image_contest/James.jpg')
    background = SimpleImage('image_contest/Holly_wood.jpg')
    background.make_as_big_as(img)
    # img.show()
    # background.show()
    combined_img = combine(img, background)
    combined_img.show()


def combine(fg, bg):
    """
    :param fg: SimpleImage, green screen figure image.
    :param bg: SimpleImage, the background image.
    :return: SimpleImage, the green screen pixels are replaced by pixels of background image
    """
    for y in range(bg.height):
        for x in range(bg.width):
            pixel_fg = fg.get_pixel(x, y)
            avg = (pixel_fg.red + pixel_fg.blue + pixel_fg.green) // 3
            total = pixel_fg.red + pixel_fg.blue + pixel_fg.green
            if pixel_fg.green > avg * THRESHOLD and total > BLACK_PIXEL:
                pixel_bg = bg.get_pixel(x, y)
                pixel_fg.red = pixel_bg.red
                pixel_fg.blue = pixel_bg.blue
                pixel_fg.green = pixel_bg.green
    return fg


if __name__ == '__main__':
    main()
