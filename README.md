ImageSearchLibrary is a library dedicated to GUI management.
========================================================

The purpose of this module is to bring to Robot Framework user a way to do image recognition.
This module has been created in 4 different parts.
    - Image recognition
    - Window focus
    - Mouse control
    - Keyboard input

It can be installed using pip:
    python -m pip install ImageRobot

With this module you will be able to do the basics of image recognition using RF.


Image recognition
========================================================

Image recognition example in Robot Framework:

    ${img}= | Set Variable | .${/}google.png
    ImageRobot.Click Image | ${img}

In this example, your Robot will look for the image at the path "./google.png" and do a left-click on it.

You can find other tools like the function "wait_until_image_appear" which will wait a certain amount of time
before going in timeout. Example :

    ${img}= | Set Variable | .${/}google.png
    ImageRobot.Wait Until Image Appear | ${img} | timeout=30

If the image has not been found in the next 30 seconds, the Robot will show a failure message telling
that it did not happen.


Window focus
========================================================


Mouse control
========================================================


Keyboard input
========================================================
