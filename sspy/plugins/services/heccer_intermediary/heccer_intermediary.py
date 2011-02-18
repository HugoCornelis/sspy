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

        self._method = ""


        if initializers is not None:

            if initializers.has_hey('arguments'):

                self._ParseArguments( initializers['arguments'])



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

#---------------------------------------------------------------------------

    def GetArguments(self):

        return self._arguments


    def _ParseInitializers(self, initializers):
        """
        @brief Parses the initializers

        Note that is only takes the first set to create a single intermediary.
        """
        try:
            
            items = initializers.items()

        except AttributeError, e:

            return None

        i = initializers[0]
            
        if i.has_key('arguments'):

            args = i['arguments']
                
            self._ParseArguments(args)

#---------------------------------------------------------------------------            

    def _ParseArguments(self, arguments):
        """

        """
        try:
            
            items = arguments.items()

        except AttributeError, e:

            return None
        
        method = ""
        
        comp2mech = []

        num_compartments = -1

        compartments = []

        a = arguments[0]

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

        self._intermediary = Intermediary(comp2mech, compartments)

#---------------------------------------------------------------------------

    def _CreateCompartmentArray(self, compartments):

        comps = []

        try:
            
            items = compartments.items()

        
        except AttributeError, e:

            return None

        for c in compartments:

            comp = self._CreateCompartmentArray()

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

            pdb.set_trace()
            
        return None

