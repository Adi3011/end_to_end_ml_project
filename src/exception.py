import sys
import logging

def error_message_details(error, error_detail:sys):
    ''' this will give what exception, where and what type of exception has occured'''
    _ , _ , exc_tb = error_detail.exc_info()  
    file_name = exc_tb.tb_frame.f_code.co_filename  # will be able to get file_name where exception occured
    error_message = "Error occured in python scrupt name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    
    return error_message
    
    
class CustomException(Exception):
    def __init__(self,error_message, error_detail:sys):
        super().__init__(error_message)   
        self.error_message = error_message_details(error_message, error_detail=error_detail)
        
    def __str__(self):
        return self.error_message