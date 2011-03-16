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

    from g3.nmc import ModelContainer
    
except ImportError, e:

    sys.exit("Error importing the Neurospaces Model Container Python module: %s\n" % e)



class Service:

#---------------------------------------------------------------------------
    def __init__(self, name="Untitled Model Container", plugin=None,
                 arguments=None, verbose=False):

        self._name = name

        self._plugin_data = plugin


#---------------------------------------------------------------------------


    def GetCore(self):

        return None
    
#---------------------------------------------------------------------------

    def GetName(self):

        return self._name

    def GetType(self):

        return self._plugin_data.GetName()

#---------------------------------------------------------------------------

    def GetModuleName(self):

        return self._plugin_data.GetName()

#---------------------------------------------------------------------------

    def GetArguments(self):

        return self._arguments

