"""!

This file contains all of the exception objects used
to handle errors.
"""

class ScheduleeCreateError(Exception):
    """

    """
    def __init__(self,msg):
        self.msg = msg
    
    def __str__(self):

        error_msg = "Failed to create a schedulee\n %s : %s" % (self.msg, self.value)
        
        return error_msg

