"""!
@file schedulee.py

This file contains the implementation for a basic schedulee.
This was formerly called SimpleHeccer in a previous implementation.
The name is kept general since it will become pluggable. This class
mainly functions as an abstraction to handle error checking
and strict typing. 
"""

import errors

#
# Should probably be a way to automatically update this list
# depending on the types of plugins present but not going to think
# of that yet
#
schedulee_types = ['solver', 'input', 'output']

class Schedulee:
    """!
    @brief Abstraction class for schedulee objects.
    """

#---------------------------------------------------------------------------

    def __init__(self, schedulee=None, schedulee_type=None):


        if schedulee is None:

            raise errors.ScheduleeError("Not defined")

        if schedulee_type is None:

            raise errors.ScheduleeError("Type not defined")

        if schedulee_type not in schedulee_types:

            raise errors.ScheduleeError("Invalid type '%s'" % schedulee_type)
        

        self._schedulees_type = schedulee_type

        self._schedulee = schedulee

        self.type = schedulee_type 

#---------------------------------------------------------------------------

    def GetCore(self):
        """

        """
        return self._schedulee


    def GetType(self):

        return self._type

#---------------------------------------------------------------------------

    def New(self, model, name, filename):
        """
        not needed?
        """
        pass


#---------------------------------------------------------------------------

    def Pause(self):
        """
        not sure how this will work
        """
        pass

#---------------------------------------------------------------------------

    def Step(self):

        self._schedulee.Step()

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
    

    
