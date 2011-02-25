"""!

This file contains all of the exception objects used
to handle errors.
"""
from exceptions import Exception



#---------------------------------------------------------------------------

class InputError(Exception):
    """
    @brief Used to report errors with output objects
    """
    def __init__(self,msg):
        self.msg = msg
    
    def __str__(self):

        error_msg = "Input object Error: %s" % (self.msg)

        if not self.value is None and self.value != "":

            error_msg = error_msg + ", " + self.value
        
        return error_msg

#---------------------------------------------------------------------------

class OutputError(Exception):
    """
    @brief Used to report errors with output objects
    """
    def __init__(self,msg):
        self.msg = msg
    
    def __str__(self):

        error_msg = "Output object Error: %s" % (self.msg)

        if not self.value is None and self.value != "":

            error_msg = error_msg + ", " + self.value
        
        return error_msg

#---------------------------------------------------------------------------

class PluginDirectoryError(Exception):
    """

    """
    def __init__(self,msg):
        self.msg = msg
    
    def __str__(self):

        error_msg = "Plugin Error: %s" % (self.msg)

        if not self.value is None and self.value != "":

            error_msg = error_msg + ", " + self.value
        
        return error_msg

#---------------------------------------------------------------------------

class PluginFileError(Exception):
    """

    """
    def __init__(self,msg):
        self.msg = msg
    
    def __str__(self):

        error_msg = "Plugin Error: %s" % (self.msg)

        if not self.value is None and self.value != "":

            error_msg = error_msg + ", " + self.value
        
        return error_msg

#---------------------------------------------------------------------------

class PluginError(Exception):
    """

    """
    def __init__(self,msg):
        self.msg = msg
    
    def __str__(self):

        error_msg = "Plugin Error: %s" % (self.msg)

        if not self.value is None and self.value != "":

            error_msg = error_msg + ", " + self.value
        
        return error_msg

#---------------------------------------------------------------------------

class ScheduleeError(Exception):
    """

    """
    def __init__(self,msg):
        self.msg = msg
    
    def __str__(self):

        error_msg = "Schedulee Error: %s" % (self.msg)
        
        return error_msg

#---------------------------------------------------------------------------

class ScheduleeCreateError(Exception):
    """

    """
    def __init__(self,msg):
        self.msg = msg
    
    def __str__(self):

        error_msg = "Failed to create a schedulee\n %s : %s" % (self.msg, self.value)
        
        return error_msg

#---------------------------------------------------------------------------

class ScheduleError(Exception):
    """

    """
    def __init__(self,msg):
        self.msg = msg
    
    def __str__(self):

        error_msg = "Specification Error: %s" % (self.msg)
        
        return error_msg

#---------------------------------------------------------------------------

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

#---------------------------------------------------------------------------


class ServiceError(Exception):
    """

    """
    def __init__(self,msg):
        self.msg = msg
    
    def __str__(self):

        error_msg = "Service Error: %s" % (self.msg)

        return error_msg


#---------------------------------------------------------------------------
    
