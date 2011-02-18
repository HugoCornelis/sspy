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
    def __init__(self, name="Untitled Heccer Intermediary", plugin_name=None,
                 initializers=None, verbose=False):

        self._name = name

        self.verbose = verbose

        self._intermediary = None

        self._method = ""

        argument_set = []
        
        if initializers is not None:

            try:

                argument_set = initializers[0]['arguments']

            except (IndexError, AttributeError, KeyError), e:

                raise Exception("Invalid Service arguments, cannot create Heccer Intermediary: %s" % e)

            self._ParseArguments(argument_set)

#---------------------------------------------------------------------------

    def GetCore(self):
        """
        @brief Returns the constructed Heccer intermediary
        """
        return self._intermediary
    
#---------------------------------------------------------------------------

    def GetName(self):

        return self._name

#---------------------------------------------------------------------------

    def GetModuleName(self):

        return self._module_name


    def GetType(self):

        return ""

#---------------------------------------------------------------------------

    def GetArguments(self):

        return self._arguments

#---------------------------------------------------------------------------            

    def _ParseArguments(self, arguments):
        """

        """
        try:
            
            a = arguments[0]

        except IndexError, e:

            raise Exception("Invalid arguments, cannot create Heccer Intermediary: %s", e)
        
        method = ""
        
        comp2mech = []

        num_compartments = -1

        compartments = []

        if a.has_key('method'):

            method = a['method']

        if a.has_key('comp2mech'):

            comp2mech = a['comp2mech'] 
            
        if a.has_key('iCompartments'):

            # Probably won't need this since I can determine
            # the number of compartments easily.
            num_compartments = a['iCompartments']
                
        if a.has_key('compartments'):

            compartments = self._CreateCompartmentArray(a['compartments'])

        # Sets the arguments so we can retrieve them
        self._arguments = a

        self._intermediary = Intermediary(compartments, comp2mech)

        
#---------------------------------------------------------------------------

    def _CreateCompartmentArray(self, compartments):

        compartment_list = []

        try:
            
            for c in compartments:

                comp = Compartment()

                if c.has_key('dCm'):

                    comp.dCm = c['dCm']

                if c.has_key('dEm'):

                    comp.dEm = c['dEm']
                
                if c.has_key('dInitVm'):

                    comp.dInitVm = c['dInitVm']
                
                if c.has_key('dRa'):

                    comp.dRa = c['dRa']

                if c.has_key('dRm'):

                    comp.dRm = c['dRm']

                compartment_list.append(comp)

        except TypeError, e:

            raise Exception("Invalid arguments, cannot create Heccer Intermediary: %s", e)
            
        return compartment_list

