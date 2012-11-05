"""
This is the solver plugin for DES to interact with
the interface of SSPy.
"""
import os
import pdb
import sys

try:
    
    from heccer.des import DES

except ImportError, e:

    sys.exit("Error importing the Heccer Python module: %s\n" % e)


class EventDistributor:

#---------------------------------------------------------------------------

    def __init__(self,  name="Untitled DES", plugin=None, 
                 arguments=None, verbose=False):
        """

        Should be able to pass the scheduler and use it as
        an internal member here.
        """
        self._name = name

        self._model_name = name

        self._plugin_data = plugin

        self.verbose = verbose
        
        self._des = None

        self._module_name = None

        self.time_step = None

        self._arguments = {}
                    
        self._compiled = False

        # this is just to keep track of granularity printing
        self.current_step = 0

      #  self._ParseConstructorSettings(constructor_settings)

#---------------------------------------------------------------------------
        
    def Initialize(self):

        self.current_step = 0
        
        self._des.Initiate()

#---------------------------------------------------------------------------

    def GetObject(self):

        return self._des

#---------------------------------------------------------------------------

    def GetName(self):

        return self._name

#---------------------------------------------------------------------------


    def SetTimeStep(self, time_step):
        """
        @brief Sets the des plugin time step
        """
 

        self.time_step = time_step

#---------------------------------------------------------------------------

    def GetTimeStep(self):
        """
        @brief Just returns the time step used for the schedulee
        """
    
        return self.time_step
    
#---------------------------------------------------------------------------

    def GetType(self):

        return self._plugin_data.GetName()


#---------------------------------------------------------------------------

    def SetConfiguration(self, config):

        pass

        

#---------------------------------------------------------------------------

    def Compile(self):
        """
        @brief 
        """
        if self._compiled is False:

            self._heccer.CompileAll()

            self._compiled = True

#---------------------------------------------------------------------------

    def IsCompiled(self):

        return self._compiled

#---------------------------------------------------------------------------

    def Connect(self, service=None):
        """!
        @brief Connects a service to the this solver

        Compatible services need to be coded into this method.

        Much like the ns-sli, the heccer object can only really
        be created when we know which service it will be connected
        to.
        """

        if not service:

            raise Exception("No service to connect to event simulator (DES) '%s'" % self.GetName())


        service_type = service.GetType()


        if service_type == "model_container":

            model_container = service.GetObject()

            if not model_container:

                raise Exception("Model Container is not defined")

            else:

                if self.verbose:

                    print "Connecting service '%s' to event distributor '%s'" % (service.GetName(), self._name)

                try:

                    self._des.Connect(model_source=model_container)

                except Exception, e:

                    raise Exception("Event distributor connection error: %s" % e)                    

        else:

            raise Exception("Incompatible Service '%s' of type '%s', can't connect event distributor to this" % (service.GetName(), service.GetType()))



#---------------------------------------------------------------------------

    def SetModelName(self, model_name):
        """!
        @brief Sets the model name for the solver to connect to

        Since a solver can target a particular part of the model
        to solve we need to set this field to let it know which.
        It is not used until heccer connection. 
        """
        self._model_name = model_name


#---------------------------------------------------------------------------

    def Finish(self):

        self._des.Finish()

#---------------------------------------------------------------------------

    def Name(self):

        return self._name


#---------------------------------------------------------------------------
        
    def Output(self, serial, field):

        print "Serial and field is %s:%s" % (serial, field)

#---------------------------------------------------------------------------

    def Run(self, time):

        print "Simulation time is %s" % time

#---------------------------------------------------------------------------

    def Step(self, time=None):
        """

        """
        if self._des is not None:

            self._des.Step(time)

            self.current_step += 1
        else:

            raise Exception("No simulation time given")

#---------------------------------------------------------------------------

    def Reset(self):
        """
        Performs a reset on the solver object.
        """
        
        self.Initialize()

#---------------------------------------------------------------------------

    def _ParseArguments(self, arguments=None):

        pass

#---------------------------------------------------------------------------




