#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime

__all__ = ["region_grabber", "search_image_in_area", "click_image", "search_image", "search_image_loop"]

import cv2
import numpy as np
import pyautogui
import random
import time
import platform
import subprocess


is_retina = False
if platform.system() == "Darwin":
    is_retina = subprocess.call("system_profiler SPDisplaysDataType | grep 'retina'", shell=True)




def region_grabber(region):
    ''' Grab a region (topx, topy, bottomx, bottomy) to the tuple (topx, topy, width, height).

    input : a tuple containing the 4 coordinates of the region to capture

    output : a PIL image of the area selected.

    '''
    if is_retina: region = [n * 2 for n in region]
    x1 = region[0]
    y1 = region[1]
    width = region[2] - x1
    height = region[3] - y1

    return pyautogui.screenshot(region=(x1, y1, width, height))


def search_image_in_area(image, x1, y1, x2, y2, precision=0.8, im=None):
    '''

    Searchs for an image within an area

    input :
        image : path to the image file (see opencv imread for supported types)
        x1 : top left x value
        y1 : top left y value
        x2 : bottom right x value
        y2 : bottom right y value
        precision : the higher, the lesser tolerant and fewer false positives are found default is 0.8
        im : a PIL image, usefull if you intend to search the same unchanging region for several elements

    returns :
        the top left corner coordinates of the element if found as an array [x,y] or [-1,-1] if not
    '''

    if im is None:
        im = region_grabber(region=(x1, y1, x2, y2))
        if is_retina:
            im.thumbnail((round(im.size[0] * 0.5), round(im.size[1] * 0.5)))
        # im.save('testarea.png') usefull for debugging purposes, this will save the captured region as "testarea.png"

    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return [-1, -1]
    return max_loc





def click_image(image, pos, action="left"):
    ''' Click in the middle of the image. By default, does a left click.

    It needs the image to calculate the center of it.
    The << pos >> variable consists in the position found by the << search_image >> - like functions.
    It represents the top left corner position.

    input :
        image : is the path to the image file (see opencv imread for supported types).
        pos : is the array containing the position of the top left corner of the image [x, y].
        action : is the button of the mouse to activate : "left" "right" "middle", see pyautogui.click documentation for more info.
    '''

    img = cv2.imread(image)
    height, width, channels = img.shape
    pyautogui.moveTo(pos[0] + width / 2, pos[1] + height / 2)
    pyautogui.click(button=action)





def search_image(image, precision=0.8):
    ''' Search for the image on the screen.

    The precision means that the image should correspond at a certain percent.
    For example, with the default precision which is 0.8, it means that the image
    to find should correspond at 80% to the given image.

    input :
        image : is the path to the image file (see opencv imread for supported types).
        precision : the higher, the lesser tolerant and fewer false positives are found. By default, 0.8.

    returns :
        the top left corner coordinates of the element if found as an array [x,y] or [-1,-1] if not
    '''
    im = pyautogui.screenshot()
    if is_retina:
        im.thumbnail((round(im.size[0] * 0.5), round(im.size[1] * 0.5)))
    # im.save('testarea.png') useful for debugging purposes, this will save the captured region as "testarea.png"
    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
    template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return [-1, -1]
    return max_loc



def search_image_loop(image, timesample, precision=0.8, timeout=60):
    ''' Search for the image on screen continuously until it is found or timeout expired.

    input :
        image : path to the image file (see opencv imread for supported types)
        time : Waiting time after failing to find the image
        precision : the higher, the lesser tolerant and fewer false positives are found default is 0.8
        timeout : is the time ellapsed max before stop searching

    returns :
        the top left corner coordinates of the element if found as an array [x,y]

    '''
    pos = search_image(image, precision)
    time1 = time.clock()

    while pos[0] == -1:
        time.sleep(timesample)
        pos = search_image(image, precision)

        if time.clock() - time1 > timeout:
            return -1
    return pos


'''
Searchs for an image on screen continuously until it's found or max number of samples reached.

input :
image : path to the image file (see opencv imread for supported types)
time : Waiting time after failing to find the image
maxSamples: maximum number of samples before function times out.
precision : the higher, the lesser tolerant and fewer false positives are found default is 0.8

returns :
the top left corner coordinates of the element if found as an array [x,y]

'''


def search_image_numLoop(image, timesample, maxSamples, precision=0.8):
    pos = search_image(image, precision)
    count = 0
    while pos[0] == -1:
        time.sleep(timesample)
        pos = search_image(image, precision)
        count = count + 1
        if count > maxSamples:
            break
    return pos


'''
Searchs for an image on a region of the screen continuously until it's found.

input :
image : path to the image file (see opencv imread for supported types)
time : Waiting time after failing to find the image
x1 : top left x value
y1 : top left y value
x2 : bottom right x value
y2 : bottom right y value
precision : the higher, the lesser tolerant and fewer false positives are found default is 0.8

returns :
the top left corner coordinates of the element as an array [x,y]

'''


def search_image_in_region_loop(image, timesample, x1, y1, x2, y2, precision=0.8, timeout=60):
    pos = search_image_in_area(image, x1, y1, x2, y2, precision)

    time1 = time.clock()
    while pos[0] == -1:
        time.sleep(timesample)
        pos = search_image_in_area(image, x1, y1, x2, y2, precision)

        if time.clock() - time1 > timeout:
            return -1
    return pos


'''
Searches for an image on the screen and counts the number of occurrences.

input :
image : path to the target image file (see opencv imread for supported types)
precision : the higher, the lesser tolerant and fewer false positives are found default is 0.9

returns :
the number of times a given image appears on the screen.
optionally an output image with all the occurances boxed with a red outline.

'''


def search_image_count(image, precision=0.9):
    img_rgb = pyautogui.screenshot()
    if is_retina:
        img_rgb.thumbnail((round(img_rgb.size[0] * 0.5), round(img_rgb.size[1] * 0.5)))
    img_rgb = np.array(img_rgb)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= precision)
    count = 0
    for pt in zip(*loc[::-1]):  # Swap columns and rows
        # cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2) // Uncomment to draw boxes around found occurances
        count = count + 1
    # cv2.imwrite('result.png', img_rgb) // Uncomment to write output image with boxes drawn around occurances
    return count


def search_image_multiple(image, precision=0.8):
    img_rgb = pyautogui.screenshot()
    if is_retina:
        img_rgb.thumbnail((round(img_rgb.size[0] * 0.5), round(img_rgb.size[1] * 0.5)))
    img_rgb = np.array(img_rgb)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= precision)
    positions = []
    for pt in zip(*loc[::-1]):  # Swap columns and rows
        positions += [(pt[0] + w / 2, pt[1] + h / 2)]
    return positions


def __random_distanceandom_distance(num, rand):
    return num + rand * random.random()
