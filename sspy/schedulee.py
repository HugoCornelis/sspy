"""!
@file schedulee.py

This file contains the implementation for a basic schedulee.
This was formerly called SimpleHeccer in a previous implementation.
The name is kept general since it will become pluggable. This class
mainly functions as an abstraction to handle error checking
and strict typing. 
"""

from errors import ScheduleeCreateError


class Schedulee:

    
    def __init__(self, model, name, filename):

        self._heccer = Heccer()


    def GetCore(self):
        """

        """
        return None

    def New(self, model, name, filename):
        """
        
        """
        pass

    def Pause(self):
        """

        """
        pass
        

    def GetTimeStep(self):
        """

        """
        return None
        

    def Compile(self):

        pass

    def Output(self, serial, field):
        """

        """
        address = self._heccer.GetAddress(serial, field)

        

    def Run(self, time):

        pass

    

    
