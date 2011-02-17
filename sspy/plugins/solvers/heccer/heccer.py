"""
This is the solver plugin for Heccer to interact with
the interface of SSPy.
"""
import os
import pdb
import sys

# this should go away later when I update the
# 
sys.path.append("/usr/local/glue/swig/python")

try:

    from g3.heccer import Heccer
    
except ImportError, e:

    sys.exit("Error importing the Heccer Python module: %s\n" % e)


class Solver:

#---------------------------------------------------------------------------

    def __init__(self, verbose=False, name="Untitled solver",
                 constructor_settings=None):
        """

        Should be able to pass the scheudler and use it as
        an internal member here.
        """
        
        self._heccer = Heccer(name=name)

        

        self._service = None

        if constructor_settings.has_key('service_name'):

            self._service = constructor_settings['service_name']

        # This will probably be unneeded in python
        if constructor_settings.has_key('module_name'):

            self._module_name = constructor_settings['module_name']

        if constructor_settings.has_key('configuration'):

            configuration = constructor_settings['configuration']

            # set configuration

        time_step = 0
        
        if constructor_settings.has_key('dStep'):

            time_step = constructor_settings['dStep']

        elif constructor_settings.has_key('step'):

            time_step = constructor_settings['step']
            

        self._heccer.SetTimeStep(time_step)


        


#---------------------------------------------------------------------------

    def GetName(self):

        return self._heccer.GetName()


#---------------------------------------------------------------------------

    def SetConfiguration(self, config):

        pass

#---------------------------------------------------------------------------

    def New(self, modelname, filename):

        print "Modelname %s, Filename %s" % (modelname, filename)
        

#---------------------------------------------------------------------------

    def Advance(self):

        pass

#---------------------------------------------------------------------------

    def Compile(self):

        pass

#---------------------------------------------------------------------------

    def Connect(self, service=None):

        if not service:

            raise errors.SolverError("No service to connect to solver '%s'" % self.GetName())

#---------------------------------------------------------------------------

    def Deserialize(self, filename):

        pass

#---------------------------------------------------------------------------

    def DeserializeState(self, filename):

        pass

#---------------------------------------------------------------------------

    def Finish(self):

        pass

#---------------------------------------------------------------------------

    def Name(self):

        return self._name

#---------------------------------------------------------------------------

    def SetSolverField(self, field, value):

        pass

#---------------------------------------------------------------------------

    def GetSolverField(self, field):

        pass

#---------------------------------------------------------------------------


    def Serialize(self, filename):

        pass

#---------------------------------------------------------------------------

    def SerializeState(self, filename):

        pass

#---------------------------------------------------------------------------
        
    def Output(self, serial, field):

        print "Serial and field is %s:%s" % (serial, field)

#---------------------------------------------------------------------------

    def Run(self, time):

        print "Simulation time is %s" % time

#---------------------------------------------------------------------------

    def Step(self):

        pass

#---------------------------------------------------------------------------

    def Steps(self, steps):

        pass

  