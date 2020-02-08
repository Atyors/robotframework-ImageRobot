class RobotException(Exception):
    ''' This class has been made to implement special error messages.
    '''

    # ==================================================================================================================
    # Image errors
    # ==================================================================================================================

    def image_not_found_exception(self, image):
        ''' Throw a message when an image has not been found.

            Parameters
            ----------
            image: str
                The path to the image searched.
        '''

        raise Exception("Image \"" + str(image) + "\" not found.")


    def image_not_found_after_duration_exception(self, image, timeout):
        ''' Throw a message when an image has not been found after a certain amount of time.

            Parameters
            ----------
            image: str
                The path to the image searched.
            timeout: int
                The duration elapsed before throwing the message.
        '''

        raise Exception("Image \"" + str(image) + "\" not found after " + str(timeout) + " seconds.")


    def image_still_found_after_duration_exception(self, image, timeout):
        ''' Throw a message when an image has been found after a certain amount of time.

            Parameters
            ----------
            image: str
                The path to the image searched.
            timeout: int
                The duration elapsed before throwing the message.
        '''

        raise Exception("Image \"" + str(image) + "\" still found after " + str(timeout) + " seconds.")


    def image_format_exception(self):
        ''' Throw a message if the format set is wrong.
        '''

        raise Exception("Image format is unknown. Should be either \".png\" or \".jpg\".")


    # ==================================================================================================================
    # Environment errors
    # ==================================================================================================================

    def wrong_path_to_image_exception(self, image):
        ''' Throw a message when a path to an image has not been found.

            Parameters
            ----------
            image: str
                The path of the image searched.
        '''

        raise Exception("Wrong path to image \"" + str(image) + "\". Please ensure your path.")


    def cannot_write_on_disk_exception(self):
        ''' Throw a message when the user has not the right to write on the disk.
        '''

        raise Exception("Cannot write on disk for image manipulation.")


    def too_many_screenshots_exception(self):
        ''' Throw a message when the user has too many screenshots in the repository.
        '''

        raise Exception("Consider cleaning your repository. It seems you already have 999 screenshots.")


    # ==================================================================================================================
    # Focus errors
    # ==================================================================================================================
    
    def no_window_containing_text_exception(self, name):
        ''' Throw a message when a window containing a certain text has not been found.

            Parameters
            ----------
            name: str
                The text searched in the window names.
        '''

        raise Exception("Window containing name \"" + str(name) + "\" has not been found.")

    
    def no_window_matching_text_exception(self, name):
        ''' Throw a message when a window with an exact text has not been found.

            Parameters
            ----------
            name: str
                The exact text searched in the window names.
        '''

        raise Exception("Window with exact name \"" + str(name) + "\" has not been found.")


    def no_window_focused_exception(self):
        ''' Throw a message when no window has been focused.
        '''

        raise Exception("No handle has been focused yet. Use one of the focus functionality first.")


    # ==================================================================================================================
    # Mouse errors
    # ==================================================================================================================

    def offset_too_high_exception(self, offset, maximum_offset):
        ''' Throw a message when the offset can reach of the image boundaries.

            Parameters
            ----------
            offset: double
                The offset chosen by the user.
            maximum_offset: double
                The maximum offset possible before arrivign out of the image boundaries.
        '''

        raise Exception("Offset (" + str(offset) + ") is too high. It may cause the cursor get out of the image targeted. Maximum allowed is " + str(maximum_offset) + ".")