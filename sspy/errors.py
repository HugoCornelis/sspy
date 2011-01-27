"""!

This file contains all of the exception objects used
to handle errors.
"""
from exceptions import Exception

class ScheduleeCreateError(Exception):
    """

    """
    def __init__(self,msg):
        self.msg = msg
    
    def __str__(self):

        error_msg = "Failed to create a schedulee\n %s : %s" % (self.msg, self.value)
        
        return error_msg



class SolverError(Exception):
    """

    """
    def __init__(self,msg):
        self.msg = msg
    
    def __str__(self):

        error_msg = "Solver Error: %s" % (self.msg)

        if not self.value is None and self.value != "":

            error_msg = error_msg + ", " + self.value
        
        return error_msg

    
