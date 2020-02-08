ImageSearchLibrary is a library dedicated to GUI management.
========================================================

The purpose of this module is to bring to Robot Framework user a way to do image recognition.
This module has been created in 4 different parts:
- Image recognition
- Window focus
- Mouse control
- Keyboard input

It can be installed using pip once the folder has been downloaded:
    python -m pip install ImageRobot

With this module you will be able to do the basics of image recognition using Robot Framework.

The functions for the mouse control and the keyboard input are mostly wrapers from other libraries.


Image recognition
========================================================

Image recognition example in Robot Framework:

    ${img}= | Set Variable | .${/}google.png
    ${pos}= | ImageRobot.Search Image | ${img}

In this example, your Robot will look for the image at the path "./google.png" and return the position on the screen
where the image has been found.

If the image may appear because the loading takes time, you can use the function "wait_until_image_appear" which will 
wait a certain amount of time before going in timeout. Example:

    ${img}= | Set Variable | .${/}google.png
    ${pos}= | ImageRobot.Wait Until Image Appear | ${img} | timeout=30

If the image has not been found in the next 30 seconds, the Robot will show a failure message telling
that it did not happen. Otherwise the "pos" variable will get the position of the image found.

You can highlight the image you are looking for with the function "highlight image". If the image
is found multiple times, it will draw a rectangle arround each.

    ImageRobot.Highlight Image | ${img}

This function will save the image on the disk. If too many screenshots already exist, it will throw
an error telling to clean the repository. It happens when there is 999 screenshots in the repository
from where the robot is launched.


Window focus
========================================================

The Focus class gives you a tool to select specific windows and do action on it.
Once the window has been set in focus, it is possible to put it foreground, minimize, maximize and restore it.
Example:

    ImageRobot.Focus Window Containing | Firefox
    ImageRobot.Restore Window
    ImageRobot.Maximize Window

This sequence will check if a window containing "Firefox" in the name is found. If so it will create a focus on it
Then we restore the window. It means that if the window has been reduced in the desk bar, it will show it up again.
Finaly the Robot maximize the window making it full screen as if you clicked the maximize button.


Mouse control
========================================================

The Mouse class gives you some functions dedicated to mouse control.
You can find the classics "Click Position" - to click at specific coordinates -, "Click Image" - to click on an image
if the image has been found -, "Move Cursor To Position" - to move the cursor at specific coordinates - and so on.

If you use the click image without giving a timestamp, you will not see the cursor move before the click.


Keyboard input
========================================================

The Keyboard class gives you some functions dedicated to keyboard control.
The classic functions are available like the "Input Text" function. It does not need any locator to be used.
There is also a function named "Execute Hotkey" which gives the user a tool to use hotkeys.
Example :

    ImageRobot.Execute Hotkey | ctrl+shift+escape

This line will open the task manager.