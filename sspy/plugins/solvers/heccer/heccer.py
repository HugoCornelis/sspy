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
    from g3.heccer import HeccerOptions

except ImportError, e:

    sys.exit("Error importing the Heccer Python module: %s\n" % e)


class Solver:

#---------------------------------------------------------------------------

    def __init__(self,  name="Untitled solver", plugin=None, 
                 constructor_settings=None, verbose=False):
        """

        Should be able to pass the scheudler and use it as
        an internal member here.
        """

        self._plugin_data = plugin
        
        self._heccer = None

        self._service = None

        self._compiled = False


        time_step = 0
        
        if constructor_settings.has_key('service_name'):

            self._service_name = constructor_settings['service_name']

        # This will probably be unneeded in python
        if constructor_settings.has_key('module_name'):

            self._module_name = constructor_settings['module_name']

        if constructor_settings.has_key('configuration'):

            self._configuration = constructor_settings['configuration']

            # set configuration
        
        if constructor_settings.has_key('dStep'):

            time_step = constructor_settings['dStep']

        elif constructor_settings.has_key('step'):

            time_step = constructor_settings['step']
            

        #self._heccer.SetTimeStep(time_step)


        


#---------------------------------------------------------------------------

    def GetName(self):

        return self._heccer.GetName()


#---------------------------------------------------------------------------

    def GetType(self):

        return self._plugin_data.GetName()


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

    def IsCompiled(self):

        return self._compiled

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

  
