import keyboard


class Keyboard(object):
    """ This class has been made to implement keyboard control while image recognition.
    """

    @staticmethod
    def input_text(text, interval=0):
        """ Simulate the type of the given text.

            If necessary can have set an interval duration between each character.

            Parameters
            ----------
            text: str
                The text to type.
            interval: double, optional
                The duration between two characters. Value is in second. Default is << 0 >>.
        """

        keyboard.write(text)

    @staticmethod
    def press_key(key):
        """ Simulate the pressure and release of a key.

            Parameters
            ----------
            key: str
                The key code to press and release.
        """

        keyboard.press(key)
        keyboard.release(key)

    @staticmethod
    def maintain_key_pressed(key):
        """ Simulate the pressure of a key until the function << release_key >> is called.

            Parameters
            ----------
            key: str
                The key code to maintain pressed.
        """

        keyboard.press(key)

    @staticmethod
    def release_key(key):
        """ Simulate the release of a key after the function << maintain_key_pressed >> has been called.

            Parameters
            ----------
            key: str
                The key code to release.
        """

        keyboard.release(key)

    @staticmethod
    def execute_hotkey(hotkey):
        """ Simulate the pressure of multiple keys in order to do a hotkey.

            Example: giving << shift+a >> as << hotkey >> variable would write a << A >> capitalized.
            Example: giving << ctrl+shift+esc >> as << hotkey >> variable would open the task manager.

            Parameters
            ----------
            hotkey: str
                A string representing a hotkey. Example: << ctrl+shit+esc >> will do the Control-Shift-Escape hotkey.
        """

        keyboard.press_and_release(hotkey)
