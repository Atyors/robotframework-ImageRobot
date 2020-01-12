import pygetwindow as gw
import re


class Focus(object):
    ''' This class has been made to implement window management in order to facilitate
        image recognition or switch windows if necessary.
    '''


    def __init__(self):
        ''' Set the initial values once the class is called.
        '''
        self.handle = None


    def focus_window_containing(self, name):
        ''' Set the found window in the foreground.

            Parameters
            ----------
            name: str
                The name or a part of the name of the searched window.
            
            Raises
            ------
            Exception
                If not any window containing the name or part of the name given has been found.
        '''

        found = False

        for title in gw.getAllTitles():
            if name in title:
                self.handle = gw.getWindowsWithTitle(title)[0]
                self.handle.activate()
                found = True
                break

        if not found:
            raise Exception("Window containing name \"" + str(name) + "\" has not been found.")


    def focus_window_with_exact_name(self, name):
        ''' Set the found window in the foreground.

            Parameters
            ----------
            name: str
                The exact name of the searched window.
            
            Raises
            ------
            Exception
                If not any window with the name given has been found.
        '''

        found = False

        for title in gw.getAllTitles():
            if name == title:
                self.handle = gw.getWindowsWithTitle(title)[0]
                self.handle.activate()
                found = True
                break

        if not found:
            raise Exception("Window with exact name \"" + str(name) + "\" has not been found.")


    def maximize_window(self):
        ''' Maximize the window focused.

            Raises
            ------
            Exception
                If not any window has been focused earlier.
        '''

        try:
            self.handle.maximize()
        except AttributeError:
            raise Exception("No handle has been focused yet. Use one of the focus functionality first.")

    
    def minimize_window(self):
        ''' Minimize the window focused.

            Raises
            ------
            Exception
                If not any window has been focused earlier.
        '''

        try:
            self.handle.minimize()
        except AttributeError:
            raise Exception("No handle has been focused yet. Use one of the focus functionality first.")

    
    def restore_window(self):
        ''' Restore the window focused.

            Raises
            ------
            Exception
                If not any window has been focused earlier.
        '''

        try:
            self.handle.restore()
        except AttributeError:
            raise Exception("No handle has been focused yet. Use one of the focus functionality first.")