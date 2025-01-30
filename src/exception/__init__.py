import sys
import logging

def error_message_detail(error: Exception, error_detail: sys) -> str:
    """
    Extracts detailed error information including file name, line number and error message.
    
    :param error: the exception that occurred
    :param error_detail: the system module to access the traceback details
    :return: a formatted string containing the detailed error information
    """
    
    # extract the traceback details (exception information )
    _, _, exc_tb = error_detail.exc_info()
    
    # get the filename where the exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    # create a formatted error message with file_name, line number and error message
    line_number = exc_tb.tb_lineno
    
    error_message = f"Error occured in python script: [{file_name} at line number {line_number}]: {str(error)}"
    
    # log the error for better tracking
    logging.error(error_message)
    
    return error_message


class MyException(Exception):
    """
    Custom exception class for handling errors
    """
    
    def __init__(self, error_message: str, error_detail: sys):
        
        # call base constructor class with error message
        super().__init__(error_message)
        
        # format the detailed error_message_detail function
        self.error_message = error_message_detail(error_message, error_detail)
        
    
    def __str__(self) -> str:
        """
        Represents string representation of error message.
        """
        return self.error_message