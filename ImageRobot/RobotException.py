class RobotException(Exception):
    ''' This class has been made to implement special error messages.
    '''

    # ==================================================================================================================
    # Image errors
    # ==================================================================================================================

    def image_not_found_exception(self, image):
        raise Exception("Image \"" + str(image) + "\" not found.")


    def image_not_found_after_duration_exception(self, image, timeout):
        raise Exception("Image \"" + str(image) + "\" not found after " + str(timeout) + " seconds.")


    def image_still_found_after_duration_exception(self, image, timeout):
        raise Exception("Image \"" + str(image) + "\" still found after " + str(timeout) + " seconds.")


    def image_format_exception(self):
        raise Exception("Image format is wrong. Should be either \".png\" or \".jpg\".")


    # ==================================================================================================================
    # Environment errors
    # ==================================================================================================================

    def wrong_path_to_image_exception(self, image):
        raise Exception("Wrong path to image \"" + str(image) + "\". Please ensure your path.")


    def cannot_write_on_disk_exception(self):
        raise Exception("Cannot write on disk for image manipulation.")


    def too_many_screenshots_exception(self):
        raise Exception("Consider cleaning your repository. It seems you already have 999 screenshots.")
