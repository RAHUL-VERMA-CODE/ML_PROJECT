import sys  # Used to get exception details (file name, line number)


# Returns a detailed error message
def error_message_detail(error, error_detail: sys):

    # Get exception traceback
    _, _, exc_tb = error_detail.exc_info()

    # Get the file name where the error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Create formatted error message
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,
        exc_tb.tb_lineno,
        str(error)
    )

    return error_message


# Custom exception class
class CustomException(Exception):

    # Constructor
    def __init__(self, error_message, error_detail: sys):

        # Call parent Exception constructor
        super().__init__(error_message)

        # Store detailed error message
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    # Return error message when exception is printed
    def __str__(self):
        return self.error_message