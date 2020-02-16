# RobotFramework-ImageRobot

- [Updates](#updates)
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Image recognition](#image-recognition)
- [Installation](#installation)
- [Window focus](#window-focus)
- [Mouse control](#mouse-control)
- [Keyboard input](#keyboard-input)


## Updates

- Fix "setup.py" for installation not properly working
- Fix timestamp usage for "click_image" function
- Fix timeout usage for "click_image" function
- Add "center" parameter in "search_image" function
- Add "set_region" function
- Add "release_region" function


## Introduction

The purpose of this module is to bring to Robot Framework user a way to do image recognition.
This module has been created in 4 different parts:
- Image recognition
- Window focus
- Mouse control
- Keyboard input

With this module you will be able to do the basics of image recognition using Robot Framework.

The functions for the mouse control and the keyboard input are mostly wrapers from other libraries.


## Requirements

Python version: 3.6+

Modules required:
- keyboard
- numpy
- opencv-python
- pyautogui
- pygetwindow
- robotframework


## Installation

It can simply be installed using pip once the project has been cloned or downloaded:
    python -m pip install ImageRobot


## Image recognition

Image recognition example in Robot Framework:

    ${img}=  BuiltIn.Set Variable  .${/}google.png
    ${pos}=  ImageRobot.Search Image  ${img}

In this example, your Robot will look for the image at the path "./google.png" and return the position on the screen
where the image has been found.

If the image may appear because the loading takes time, you can use the "wait_until_image_appear" function which will 
wait a certain amount of time before going in timeout. Example:

    ${img}=  BuiltIn.Set Variable  .${/}google.png
    ${pos}=  ImageRobot.Wait Until Image Appear  ${img}  timeout=30

If the image has not been found in the next 30 seconds, the Robot will show a failure message telling
that it did not happen. Otherwise the "pos" variable will get the position of the image found.

You can highlight the image you are looking for with the "highlight image" function. If the image
is found multiple times, it will draw a rectangle arround each.

    ImageRobot.Highlight Image  ${img}

This function will save the image on the disk. If too many screenshots already exist, it will throw
an error telling to clean the repository. It happens when there is 999 screenshots in the repository
from where the robot is launched.

If you need to find an image in a specific region, in order to optimize performance you can use the
"set region" function. The screenshot will be taken for only the part until it has been released with
"release region".

    ImageRobot.Set Region  0  0  500  500
    ImageRobot.Highlight Image  ${img}
    ImageRobot.Release Region

This sequence will try to find and highlight the image in the upper-left region of the screen. Then it releases the region
so next searchs will be done on the whole screen.


## Window focus

The Focus class gives you a tool to select specific windows and do action on it.
Once the window has been set in focus, it is possible to put it foreground, minimize, maximize and restore it.
Example:

    ImageRobot.Focus Window Containing  Firefox
    ImageRobot.Restore Window
    ImageRobot.Maximize Window

This sequence will check if a window containing "Firefox" in the name is found. If so it will create a focus on it
Then we restore the window. It means that if the window has been reduced in the desk bar, it will show it up again.
Finaly the Robot maximize the window making it full screen as if you clicked the maximize button.


## Mouse control

The Mouse class gives you some functions dedicated to mouse control.
You can find the classics "Click Position" - to click at specific coordinates -, "Click Image" - to click on an image
if the image has been found -, "Move Cursor To Position" - to move the cursor at specific coordinates - and so on.

If you use the click image without giving a timestamp, you will not see the cursor move before the click.

Even if the "Set Region" function has been used, the mouse will not use it. So it is preferable to use a sequence of
actions like the example above:

    ImageRobot.Set Region  0  0  960  1080
    ${pos}=  ImageRobot.Search Image  ${img}  center=True
    BuiltIn.Run Keyword If  ${pos}[0] != -1  ImageRobot.Click Position  ${pos}[0]  ${pos}[1]
    ImageRobot.Release Region

With the "Set Region" we cut the left half part of a screen width 1920 * 1080. We search in this cut part.
If the value returned is different than "-1", it means the image has been found so we can click at the position returned.
Finally we release the region set.


## Keyboard input

The Keyboard class gives you some functions dedicated to keyboard control.
The classic functions are available like the "Input Text" function. It does not need any locator to be used.
There is also a function named "Execute Hotkey" which gives the user a tool to use hotkeys.
Example :

    ImageRobot.Execute Hotkey  ctrl+shift+escape

This line will open the task manager.
