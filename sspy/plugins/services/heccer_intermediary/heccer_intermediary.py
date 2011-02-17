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
    from g3.heccer import Compartment
    from g3.heccer import Intermediary
    
except ImportError, e:

    sys.exit("Error importing the Heccer Python module: %s\n" % e)



class Service:

#---------------------------------------------------------------------------
    def __init__(self, verbose=False, name="Untitled Heccer Intermediary", initializers=None):

        self._name = name

        self.verbose = verbose

        self._intermediary = None


#---------------------------------------------------------------------------


    def GetCore(self):

        return None
    
#---------------------------------------------------------------------------

    def GetName(self):

        return self._name

#---------------------------------------------------------------------------

    def GetModuleName(self):

        return self._module_name

#---------------------------------------------------------------------------

    def GetArguments(self):

        return self._arguments

