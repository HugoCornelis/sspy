"""!


"""

class SSPYInterfaceError(Exception):

    pass



def parse(arg):
    """

    Borrowed from the Python.org Turtle Shell example
    
    Convert a series of zero or more numbers to an argument tuple
    """
    return tuple(map(int, arg.split()))

        
#---------------------------------------------------------------------------


class SSPYInterface:
    """!

    SSPy is a stateless program that simply loads and runs a
    declarative schedule. The SSPy interface creates states
    for working with sspy internal services, solvers, inputs,
    and outputs dynamically.
    """
    def __init__(self, scheduler=None):

        if scheduler is None:

            raise SSPYInterfaceError("No valid sspy object to interface to")

        self.scheduler = scheduler

        self.cwe
        
#---------------------------------------------------------------------------


    def set_cwe(self, element):

        self.cwe = cwe

#---------------------------------------------------------------------------

    def get_cwe(self, element):

        return self.cwe 
        

#---------------------------------------------------------------------------

    def run(self, arg):
    
        time = float(arg)

        try:

            self.scheduler.Run(time)

        except Exception, e:

            print "%s" % e

#---------------------------------------------------------------------------
