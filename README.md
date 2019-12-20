ImageSearchLibrary is a library dedicated to GUI management.
========================================================

The purpose of this module is to bring to Robot Framework user a way to do image recognition.

It can be installed using pip:
    pip install ImageRobot

With this module you will be able to do the basics of image recognition using RF.

Image recognition example in Robot Framework:

    ${img}= | Set Variable | .${/}google.png
    ImageRobot.Click Image | ${img}

In this example, your Robot will look for the image at the path "./google.png" and do a left-click on it.

You can find other tools like the function "search_image_until" which will wait a certain amount of time
before going in timeout. Example :

    ${img}= | Set Variable | .${/}google.png
    ImageRobot.Search Image Until | ${img} | timeout=30

If the image has not been found in the next 30 seconds, the Robot will show a failure message telling
that it did not happen.
