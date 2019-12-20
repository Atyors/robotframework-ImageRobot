import pyautogui

class Keyboard(object):
    '''
        This class has been made to implement keyboard control while image recognition.
    '''

    def input_text(self, text, interval=0):
        ''' Simulate the type of the given text.

            If necessary can have set an interval duration between each character.

            Parameters
            ----------
            text : str
                The text to type.
            interval : double, optional
                The duration between two characters. Value is in second. Default is << 0 >>.
        '''

        pyautogui.typewrite(text, interval)


    def maintain_key_pressed(self, key):
        ''' Simulate the pressure of a key until the function << release_key >> is called.

            The key list can be found at this link : https://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys

            Parameters
            ----------
            key : str
                The key code to maintain pressed.
        '''

        pyautogui.keyDown(key)

    
    def release_key(self, key):
        ''' Simulate the release of a key after the function << maintain_key_pressed >> has been called.

            The key list can be found at this link : https://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys

            Parameters
            ----------
            key : str
                The key to release.
        '''

        pyautogui.keyUp(key)

    
    def execute_hotkey(self, *keys):
        ''' Simulate the pressure of multiple keys in order to do a hotkey.

            Parameters
            ----------
            *keys : str(s)
                One or multiple str representing a hotkey. Example: << ctrl, shit, esc >> will do the Control-Shift-Escape hotkey.
        '''
        
        pyautogui.hotkey(*keys)
