from ImageRobot.Image import Image

import pyautogui
import cv2


class Mouse(object):
    '''
        This class has been made to implement mouse control while image recognition.
    '''


    def click_image(self, image, precision=0.8, timeout=10, action="left"):
        ''' Simulate click in the middle of the given image.

            If the image is not found, when the timeout is elapsed, an error is thrown.

            Parameters
            ----------
            image : str
                The path to the image we are looking for.
            precision : double, optionnal
                The percentage of recognition to use. Default is << 0.8 >>, meaning 80% similar.
            timeout : int, optionnal
                The duration elapsed before raising an error. Value is in second. Default is << 10 >> seconds.
            action: str, optionnal
                The action to do on the image if it is found. By default is a << left >> click action.

            Raises
            ------
            Exception
                If the image has not been found after the duration set in the timeout parameter is elapsed.
                The exception is raised by the function << search_image_until >>.
        '''

        self.move_cursor_to_image(image, precision, timeout, 0)
        pyautogui.click(button=action)


    def move_cursor_to_image(self, image, precision=0.8, timeout=10, timestamp=0.2):
        ''' Move the cursor in the middle of the given image.

            If the image is not found, when the timeout is elapsed, an error is thrown.

            Parameters
            ----------
            image : str
                The path to the image we are looking for.
            precision : double, optionnal
                The percentage of recognition to use. Default is << 0.8 >>, meaning 80% similar.
            timeout : int, optionnal
                The duration elapsed before raising an error. Value is in second. Default is << 10 >> seconds.
            timestamp: double, optionnal
                The time the movement takes to move from the current position to the found position.

            Raises
            ------
            Exception
                If the image has not been found after the duration set in the timeout parameter is elapsed.
                The exception is raised by the function << search_image_until >>.
        '''

        pos = Image().search_image_until(image, precision)
        img = cv2.imread(image)
        height, width, channels = img.shape
        pyautogui.moveTo(pos[0] + width / 2, pos[1] + height / 2, timestamp)