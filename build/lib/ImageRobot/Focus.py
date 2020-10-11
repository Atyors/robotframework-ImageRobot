import pygetwindow as gw

from ImageRobot.RobotException import RobotException


class Focus(object):
    """ This class has been made to implement window management in order to facilitate
        image recognition or switch windows if necessary.
    """

    handle = None

    def focus_window_containing(self, name):
        """ Set the found window in the foreground.

            Parameters
            ----------
            name: str
                The name or a part of the name of the searched window.
            
            Raises
            ------
            RobotException
                If not any window containing the name or part of the name given has been found.
        """

        for title in gw.getAllTitles():
            if name in title:
                self.handle = gw.getWindowsWithTitle(title)[0]
                self.handle.activate()
                break

        if self.handle is None:
            RobotException().no_window_containing_text_exception(name)

    def focus_window_with_exact_name(self, name):
        """ Set the found window in the foreground.

            Parameters
            ----------
            name: str
                The exact name of the searched window.
            
            Raises
            ------
            RobotException
                If not any window with the name given has been found.
        """

        for title in gw.getAllTitles():
            if name == title:
                self.handle = gw.getWindowsWithTitle(title)[0]
                self.handle.activate()
                break

        if self.handle is None:
            RobotException().no_window_matching_name_exception(name)

    def maximize_window(self):
        """ Maximize the window focused.

            Raises
            ------
            RobotException
                If not any window has been focused earlier.
        """

        try:
            self.handle.maximize()
        except AttributeError:
            RobotException().no_window_focused_exception()

    def minimize_window(self):
        """ Minimize the window focused.

            Raises
            ------
            RobotException
                If not any window has been focused earlier.
        """

        try:
            self.handle.minimize()
        except AttributeError:
            RobotException().no_window_focused_exception()

    def restore_window(self):
        """ Restore the window focused.

            Raises
            ------
            RobotException
                If not any window has been focused earlier.
        """

        try:
            self.handle.restore()
        except AttributeError:
            RobotException().no_window_focused_exception()

    def remove_focus(self):
        """ Remove the current focus.
        """

        self.handle = None
