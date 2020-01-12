import os.path
import time
import cv2
import numpy as np
import pyautogui


class Image(object):
    '''
        This class has been made to implement image recognition on the main screen.
    '''


    def __init__(self):
        ''' Set the initial values once the class is called.
        '''
        self.screenshot_name = "imagerobot-screenshot"


    def search_image(self, image, precision=0.8, debug=False):
        ''' Search for the image on the screen.

            If the image is not found throws an exception.

            Parameters
            ----------
            image : str
                The path to the image we are looking for.
            precision : double, optional
                The percentage of recognition to use. Default is << 0.8 >>, meaning 80% similar.
            debug : bool, optional
                The activation of the debug mode. If << True >> takes a screenshot of the screen. Default is << False >>.

            Raises
            ------
            Exception
                If the image has not been found.
        '''

        current_screen = pyautogui.screenshot()

        if debug:
            current_screen.save('debug_screen.png')

        img_rgb = np.array(current_screen)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

        try:
            template = cv2.imread(image, 0)
            template.shape[::-1]
        except Exception:
            raise Exception("Wrong path to image \"" + str(image) + "\". Please ensure your path.")

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        if max_val < precision:
            return [-1, -1]

        return max_loc


    def wait_until_image_appear(self, image, precision=0.8, timeout=10, timesample=0.1):
        ''' Wait until the given image appears in the screen for a given duration.

            If the image is not found, when the timeout is elapsed, an error is thrown.

            Parameters
            ----------
            image : str
                The path to the image we are looking for.
            precision : double, optional
                The percentage of recognition to use. Default is << 0.8 >>, meaning 80% similar.
            timeout : int, optional
                The duration elapsed before raising an error. Value is in second. Default is << 10 >> seconds.
            timesample: double, optional
                The duration elapsed between two checks of the image. Value is in second. Default is << 0.1 >> second.

            Raises
            ------
            Exception
                If the image has not been found after the duration set in the timeout parameter is elapsed.
        '''

        pos = self.search_image(image, precision)
        start_time = time.clock()

        while pos[0] == -1:
            time.sleep(timesample)
            pos = self.search_image(image, precision)

            if time.clock() - start_time > timeout:
                raise Exception("Image \"" + str(image) + "\" not found after " + str(timeout) + " seconds.")
        return pos


    def wait_until_image_disappear(self, image, precision=0.8, timeout=10, timesample=0.1):
            ''' Wait until the given image disappears from the screen for a given duration.

                If the image is still found, when the timeout is elapsed, an error is thrown.

                Parameters
                ----------
                image : str
                    The path to the image we are waiting to disappear.
                precision : double, optional
                    The percentage of recognition to use. Default is << 0.8 >>, meaning 80% similar.
                timeout : int, optional
                    The duration elapsed before raising an error. Value is in second. Default is << 10 >> seconds.
                timesample: double, optional
                    The duration elapsed between two checks of the image. Value is in second. Default is << 0.1 >> second.

                Raises
                ------
                Exception
                    If the image has been found after the duration set in the timeout parameter is elapsed.
            '''

            pos = self.search_image(image, precision)
            start_time = time.clock()

            while pos[0] != -1:
                time.sleep(timesample)
                pos = self.search_image(image, precision)

                if time.clock() - start_time > timeout:
                    raise Exception("Image \"" + str(image) + "\" still found after " + str(timeout) + " seconds.")
            return pos


    def search_image_multiple(self, image, precision=0.8, debug=False):
        ''' Search for an image multiple times on the screen.

            Parameters
            ----------
            image : str
                The path to the image we are looking for.
            precision : double, optional
                The percentage of recognition to use. Default is << 0.8 >>, meaning 80% similar.
            debug : bool, optional
                The activation of the debug mode. If << True >> takes a screenshot of the screen. Default is << False >>.

            Raises
            ------
            Exception
                If the image has not been found.

            Return
            ------
            positions : list of tuples
                Each tuple in the list is the middle of a found image similar to the one chosen.
        '''

        current_screen = pyautogui.screenshot()

        if debug:
            current_screen.save('debug_screen.png')

        img_rgb = np.array(current_screen)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

        try:
            template = cv2.imread(image, 0)
            w, h = template.shape[::-1]
        except Exception:
            raise Exception("Image \"" + str(image) + "\" not found.")

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= precision)

        positions = []
        for pt in zip(*loc[::-1]): # Swap columns and rows
            positions += [(pt[0] + w / 2, pt[1] + h / 2)]

        return positions


    def count_image(self, image, precision=0.8, debug=False):
        ''' Search for an image multiple times on the screen.

            Parameters
            ----------
            image : str
                The path to the image we are looking for.
            precision : double, optional
                The percentage of recognition to use. Default is << 0.8 >>, meaning 80% similar.
            debug : bool, optional
                The activation of the debug mode. If << True >> takes a screenshot of the screen. Default is << False >>.

            Raises
            ------
            Exception
                If the image has not been found.

            Return
            ------
            count : int
                The number of times the image has been found on the screen. 
        '''

        current_screen = pyautogui.screenshot()

        if debug:
            current_screen.save('debug_screen.png')

        img_rgb = np.array(current_screen)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

        try:
            template = cv2.imread(image, 0)
            w, h = template.shape[::-1]
        except Exception:
            raise Exception("Image \"" + str(image) + "\" not found.")

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= precision)

        count = 0
        for pt in zip(*loc[::-1]):
            count += 1

        return count


    def highlight_image(self, image, precision=0.8, color=(0, 0, 255), width=2, name=None, debug=False):
        ''' Highlight the searched image in the current screen.

            Take a screenshot as << tmp.png >> then read it with cv2 to keep the good colors.

            Parameters
            ----------
            image : str
                The path to the image we are looking for.
            precision : double, optional
                The percentage of recognition to use. Default is << 0.8 >>, meaning 80% similar.
            color : bgr, optional
                The color in BGR-format meaning colors are given as following : blue, green and red. Default is << (0, 0, 255) >> which is red color.
            width : int, optional
                The width of the square borders. Value is in pixel. Default is << 2 >> pixel.
            name : str, optional
                The name of the picture if given. Otherwise the name will be such as << imagerobot-screenshot-XXX.png >>. Default is << None >>.
            debug : bool, optional
                The activation of the debug mode. If << True >> takes a screenshot of the screen. Default is << False >>.

            Raises
            ------
            Exception
                Throw an error if the user launching the function cannot write on disk.
                Throw an error if the user already has 999 sreenshots in the repository.
                Throw an error if the user set a name in a wrong format without finishing by << .png >> nor << .jpg >>.

            Output
            ------
            A screenshot named << imagerobot-screenshot-XXX.png >> (or with the given name) is created with squares arround the image searched.

            Return
            ------
            The coordinates of the top-left and bottom-right corners of the rectangle drawn.
        '''

        current_screen = pyautogui.screenshot()

        try:
            current_screen.save("debug_screen.png")
            output_image = cv2.imread("debug_screen.png")
            if not debug:
                os.remove("debug_screen.png")
        except Exception:
            raise Exception("Cannot write on disk for image manipulation.")

        output_name = self.screenshot_name
        output_number = "000"

        if os.path.isfile(output_name + "-001.png") and name == None:
            for i in range(1, 1001):
                if i < 10:
                    output_number = "00" + str(i)
                elif i < 100:
                    output_number = "0" + str(i)
                else:
                    output_number = str(i)

                if i == 1000:
                    raise Exception("Consider cleaning your repository. It seems you already have 999 screenshots.")

                if not os.path.isfile(output_name + "-" + output_number + ".png"):
                    output_name = output_name + "-" + output_number + ".png"
                    break
        else:
            output_name = self.screenshot_name + "-001.png"

        if name != None:
            if str(name[-4:]).lower() == ".png" or str(name[-4:]).lower() == ".jpg":
                output_name = str(name)
            else:
                raise Exception("Image format is wrong. Should be either \".png\" or \".jpg\".")

        img_rgb = np.array(current_screen)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

        try:
            template = cv2.imread(image, 0)
            w, h = template.shape[::-1]
        except Exception:
            raise Exception("Image \"" + str(image) + "\" not found.")

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= precision)

        for pt in zip(*loc[::-1]):
            cv2.rectangle(output_image, pt, (pt[0] + w, pt[1] + h), color, width)

        cv2.imwrite(output_name, output_image)

        return (pt, (pt[0] + w, pt[1] + h))


    def search_image_in_image(self, specific_image, image_region):
        ''' WIP
        '''
        img = cv2.imread(image_region)
        height, width, channels = img.shape
        image_region_pos = self.search_image(image_region)
        pos = self.search_image_in_region(specific_image, image_region_pos[0], image_region_pos[1], image_region_pos[0] + width, image_region_pos[1] + height)

        return (pos[0] + image_region_pos[0], pos[1] + image_region_pos[1])
        # img = cv2.imread(image_region)
        # height, width, channels = img.shape
        # image_region_pos = self.wait_until_image_appear(image_region, region_precision, region_timeout)

        # start_time = time.clock()

        # pos = [-1, -1]

        # while pos[0] == -1:
        #     time.sleep(timesample)
        #     pos = self.search_image_in_region(specific_image, image_region_pos[0], image_region_pos[1], image_region_pos[0] + width, image_region_pos[1] + height)

        #     if time.clock() - start_time > specific_timeout:
        #         raise Exception("Image \"" + str(image) + "\" still found after " + str(timeout) + " seconds.")

        # return (pos[0] + image_region_pos[0], pos[1] + image_region_pos[1])


    def search_image_in_region(image, x1, y1, x2, y2, precision=0.8):
        ''' WIP 
        '''
        region = pyautogui.screenshot(region=(x1, y1, x2, y2))

        img_rgb = np.array(region)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(image, 0)
        template.shape[::-1]

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        if max_val < precision:
            return [-1, -1]

        return max_loc


    def set_screenshot_prefix(self, prefix):
        ''' Set another prefix for the screenshot name instead of << robotimage-screenshot >>.

            Parameters
            ----------
            prefix : str
                The new prefix for the screenshot names.
        '''

        self.screenshot_name = prefix