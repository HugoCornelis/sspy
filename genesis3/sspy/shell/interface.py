"""!


"""

class SSPYInterfaceError(Exception):

    pass


class SSPYInterface:
    """!

    SSPy is a stateless program that simply loads and runs a
    declarative schedule. The SSPy interface creates states
    for working with sspy internal services, solvers, inputs,
    and outputs dynamically.
    """
    def __init__(self, schedule=None):

        if schedule is None:

            raise SSPYInterfaceError("No sspy schedule created")


        self.cwe
        


