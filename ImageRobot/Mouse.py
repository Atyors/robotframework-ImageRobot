from ImageRobot.Image import Image

import cv2
import pyautogui
import random


class Mouse(object):
    '''
        This class has been made to implement mouse control while image recognition.
    '''

    def click_position(self, x, y, action="left", timestamp=0, offset=0):
        ''' Simulate click at the given position.

            If one of the value is not a number an error is thrown.

            Parameters
            ----------
            x : int, float
                The x position on the screen.
            y : int, float
                The y position on the screen.
            action: str, optional
                The action to do on the image if it is found. By default is a << left >> click action.
            offset: int, float, optional
                The distance maximum from the targeted point. Default is << 0 >>.

            Raises
            ------
            Exception
                If one of the values is not a convertible number.
        '''

        self.move_cursor_to_position(x, y, timestamp, offset)
        pyautogui.click(button=action)


    def move_cursor_to_position(self, x, y, timestamp=0.2, offset=0):
        ''' Move the cursor in the middle of the given image.

            If one of the value is not a number an error is thrown.

            Parameters
            ----------
            x : int, float
                The x position on the screen.
            y : int, float
                The y position on the screen.
            timestamp: double, optional
                The time the movement takes to move from the current position to the found position. Default is << 0.2 >> seconds.
            offset: int, float, optional
                The distance maximum from the targeted point. Default is << 0 >>.

            Raises
            ------
            Exception
                If one of the values is not a convertible number.
        '''

        try:
            x = float(x)
            y = float(y)
        except ValueError:
            raise Exception("Values \"" + str(x) + "\" and \"" + str(y) + "\" should be number types.")

        pyautogui.moveTo(x + random.uniform(0, offset), y + random.uniform(0, offset), timestamp)


    def click_image(self, image, precision=0.8, timeout=10, action="left", timestamp=0, offset=0):
        ''' Simulate click in the middle of the given image depending on the offset.

            If the image is not found, when the timeout is elapsed, an error is thrown.

            Parameters
            ----------
            image : str
                The path to the image we are looking for.
            precision : double, optional
                The percentage of recognition to use. Default is << 0.8 >>, meaning 80% similar.
            timeout : int, optional
                The duration elapsed before raising an error. Value is in second. Default is << 10 >> seconds.
            action: str, optional
                The action to do on the image if it is found. By default is a << left >> click action.
            timestamp: double, optional
                The time the movement takes to move from the current position to the found position. Default is << 0 >> second.
            offset: int, float, optional
                The distance maximum from the targeted point. Default is << 0 >>.

            Raises
            ------
            Exception
                If the image has not been found after the duration set in the timeout parameter is elapsed.
                The exception is raised by the function << wait_until_image_appear >>.
        '''

        self.move_cursor_to_image(image, precision, timeout, timestamp, offset)
        pyautogui.click(button=action)


    def move_cursor_to_image(self, image, precision=0.8, timeout=10, timestamp=0.2, offset=0):
        ''' Move the cursor in the middle of the given image depending on the offset.

            If the image is not found, when the timeout is elapsed, an error is thrown.

            Parameters
            ----------
            image : str
                The path to the image we are looking for.
            precision : double, optional
                The percentage of recognition to use. Default is << 0.8 >>, meaning 80% similar.
            timeout : int, optional
                The duration elapsed before raising an error. Value is in second. Default is << 10 >> seconds.
            timestamp: double, optional
                The time the movement takes to move from the current position to the found position.
            offset: int, float, optional
                The distance maximum from the targeted point. Default is << 0 >>.

            Raises
            ------
            Exception
                If the image has not been found after the duration set in the timeout parameter is elapsed.
                The exception is raised by the function << wait_until_image_appear >>.
            Exception
                If the offset is too high and may cause the cursor to be out of the image.
        '''

        img = cv2.imread(image)
        height, width, channels = img.shape

        maximum_offset = width / 2
        if maximum_offset > height / 2 :
            maximum_offset = height / 2
        if offset > maximum_offset:
            raise Exception("Offset is too high. It may cause the cursor be out of the image targeted. Maximum allowed is " + str(maximum_offset) + ".")

        pos = Image().wait_until_image_appear(image, precision)

        pyautogui.moveTo(pos[0] + width / 2 + random.uniform(0, offset), pos[1] + height / 2 + random.uniform(0, offset), timestamp)


    def press_click(self, x=None, y=None, action="left", duration=0):
        ''' Press the cursor at the given coordinates.

            If one of the value is not a number an error is thrown.

            Parameters
            ----------
            x : int, float, optional
                The x position on the screen. If << None >>, set the current x position. Default is << None >>.
            y : int, float, optional
                The y position on the screen. If << None >>, set the current y position. Default is << None >>.
            action: str, optional
                The action to do on the image if it is found. By default is a << left >> click action.
            duration: int, float, optional
                The duration of the pressure on the action. If << 0 >>, maintain pressure continuously. Default is << 0 >>.

            Raises
            ------
            Exception
                If one of the values is not a convertible number.
        '''

        (old_x, old_y) = pyautogui.position()
        if x == None:
            x = old_x
        if y == None:
            y = old_y
        
        try:
            x = float(x)
            y = float(y)
        except ValueError:
            raise Exception("Values \"" + str(x) + "\" and \"" + str(y) + "\" should be number types.")

        pyautogui.mouseDown(x, y, button=action, duration=duration)
        self.pressed_button = action


    def release_click(self):
        ''' Release the cursor.
        '''

        pyautogui.mouseUp(button=self.pressed_button)