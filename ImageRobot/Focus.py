import win32gui
import re


class Focus(object):
    '''
        This class has been made to implement window management in order to facilitate
        image recognition or switch windows if necessary.
    '''


    def __init__ (self):
        ''' TODO
        '''
        
        self._handle = None


    def set_foreground_window_containing(self, name):
        ''' TODO
        '''

        self._handle = None
        name_with_wildcard = ".*" + str(name) + ".*"
        win32gui.EnumWindows(self._window_enum_callback, name_with_wildcard)
        if self._handle == None:
            raise Exception("No window containing the text \"" + name + "\" has been found.")
        win32gui.SetForegroundWindow(self._handle)


    def _window_enum_callback(self, hwnd, wildcard):
        ''' TODO
        '''

        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self._handle = hwnd
