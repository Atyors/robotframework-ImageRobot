import win32gui
import re

def find_window(self, class_name, window_name=None):
    """find a window by its class_name"""
    handle = win32gui.FindWindow(class_name, window_name)
    win32gui.SetForegroundWindow(handle)
