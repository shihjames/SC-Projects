"""
File: stanCodoshop.py
Name: James Shih
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------
Remove people or abnormal objects in a certain photo.
"""

import os
import sys
import time
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    dist = (((red - pixel.red) ** 2) + ((green - pixel.green) ** 2) + ((blue - pixel.blue) ** 2)) ** (1/2)
    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    # Create three variables to add up all pixel values.
    red = 0
    green = 0
    blue = 0
    for pixel in pixels:
        red += pixel.red
        green += pixel.green
        blue += pixel.blue
    return [red // len(pixels), green // len(pixels), blue // len(pixels)]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    red_avg = get_average(pixels)[0]
    green_avg = get_average(pixels)[1]
    blue_avg = get_average(pixels)[2]
    dist = float('inf')
    # Variable 'index' represents the index of pixel in list pixels.
    best = get_pixel_dist(pixels[0], red_avg, green_avg, blue_avg)
    for pixel in pixels:
        # Set condition to renew variables.
        if get_pixel_dist(pixel, red_avg, green_avg, blue_avg) < dist:
            # Renew value of dist.
            dist = get_pixel_dist(pixel, red_avg, green_avg, blue_avg)
            # Renew value of index.
            best = pixel
    return best

    # Method 2 #
    # dist = []
    # for i in range(len(pixels)):
    #     dist.append(get_pixel_dist(pixels[i], red_avg, green_avg, blue_avg))
    # index = dist.index(min(dist))
    # best = pixels[index]
    # return best
    # End Method 2 #


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    start = time.time()
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    # Scan through all pixels.
    for x in range(width):
        for y in range(height):
            # Create a list of pixels for the function 'get_best_pixel'.
            pixels = []
            for image in images:
                pixels.append(image.get_pixel(x, y))
            # Best pixel of a certain pixel in the image.
            best = get_best_pixel(pixels)
            # Each pixel of the result image is set as best
            result.set_pixel(x, y, best)
    end = time.time()
    print(end-start)
    # Method 2 #
    # for x in range(width):
    #     for y in range(height):
    #         pixels = []
    #         result_pix = result.get_pixel(x, y)
    #         for image in images:
    #             pixels.append(image.get_pixel(x, y))
    #         best = get_best_pixel(pixels)
    #         result_pix.red = best.red
    #         result_pix.green = best.green
    #         result_pix.blue = best.blue
    # End Method 2 #
    print("Displaying image!")
    result.show()


def jpgs_in_dir(direc):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(direc):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(direc, filename))
    return filenames


def load_images(direc):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(direc)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
