"""!
@file schedulee.py

This file contains the implementation for a basic schedulee.
This was formerly called SimpleHeccer in a previous implementation.
The name is kept general since it will become pluggable. This class
mainly functions as an abstraction to handle error checking
and strict typing. 
"""

import errors

class Schedulee:
    """!
    @brief Abstraction class for schedulee objects.
    """

#---------------------------------------------------------------------------

    def __init__(self, schedulee, schedulee_type=None):

        self._schedulees_type = schedulee_type

        self._schedulee = schedulee


#---------------------------------------------------------------------------

    def GetCore(self):
        """

        """
        return self._schedulee

#---------------------------------------------------------------------------

    def New(self, model, name, filename):
        """
        
        """
        pass


#---------------------------------------------------------------------------

    def Pause(self):
        """

        """
        pass

#---------------------------------------------------------------------------        

    def GetTimeStep(self):
        """

        """
        try:
            
            return self._schedulee.GetTimeStep()

        except TypeError, e:

            return errors.ScheduleeError("Can't retrieve time step: %s" % e)

#---------------------------------------------------------------------------

    def Compile(self):

        try:

            self._schedulee.Compile()

        except Exception, e:

            raise errors.ScheduleeError("%s" % e)

#---------------------------------------------------------------------------

    def Output(self, serial, field):
        """

        """
        pass
        
#---------------------------------------------------------------------------

    def Run(self, time):

        pass


#---------------------------------------------------------------------------
    

    
