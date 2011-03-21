"""
This is the output plugin for outputting data
from connected solvers
"""
import os
import pdb
import sys

# this should go away later when I update the
# 
sys.path.append("/usr/local/glue/swig/python")

try:

    import g3.experiment.output as output

except ImportError, e:

    sys.exit("Error importing the Experiment Output Python module: %s\n" % e)



#---------------------------------------------------------------------------


class Output:

#---------------------------------------------------------------------------

    def __init__(self,  name="Untitled solver", plugin=None, 
                 arguments=None, verbose=False):

        self._name = name

        self._plugin_data = plugin

        self.verbose = verbose
        
        
        self._output_gen = None

    
        self._output_var = "output"

#---------------------------------------------------------------------------

    def AddOutput(self, output):

        pass

#---------------------------------------------------------------------------

    def AddOutputs(self, outputs):

        pass

#---------------------------------------------------------------------------

    def GetName(self):

        return self._name

#---------------------------------------------------------------------------

    def Name(self):

        return self._name
    
#---------------------------------------------------------------------------

    def GetTimeStep(self):
        """
        """
        time_step = 0.01
        
        return time_step

#---------------------------------------------------------------------------
    

    def GetType(self):

        return self._plugin_data.GetName()

#---------------------------------------------------------------------------

    def Finish(self):

        pass

#---------------------------------------------------------------------------

    def Initialize(self):

        pass
    
#---------------------------------------------------------------------------

    def Connect(self, solver):


        solver_type = solver.GetType()

        if solver_type == 'heccer':

            #
            # Here we use modelname to get the 
            # membrane potential. 
            address = solver.GetAddress(modelname, "Vm")

            self._output_gen.AddOutput(self._output_var, address) 

#---------------------------------------------------------------------------


    def Step(self, time=None):
        """

        """
        pass
        #self._output_gen.Step()


#---------------------------------------------------------------------------

    def Report(self):

        pass

#---------------------------------------------------------------------------
