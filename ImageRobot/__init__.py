"""
    This module is the entry to the subclasses used to make image recognition.
"""

from ImageRobot.version import __version__
from ImageRobot.Image import Image
from ImageRobot.Focus import Focus
from ImageRobot.Mouse import Mouse
from ImageRobot.Keyboard import Keyboard


VERSION = __version__

class ImageRobot(Image, Focus, Mouse, Keyboard):
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = VERSION