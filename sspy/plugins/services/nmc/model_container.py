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

        self.verbose = verbose

        try:
            
            self._model_container = ModelContainer()

        except Exception, e:

            raise Exception("Service Error: Can't initialize Model Container '%s', %s" % (self._name, e))

        if self._model_container is None:

            raise Exception("Service Error: Can't initialize Model Container '%s'" % (self._name))


        self._arguments = arguments

        self._ParseArguments()

#---------------------------------------------------------------------------


    def GetCore(self):
        """
        @brief Returns the constructed model container
        """
        return self._model_container
    
#---------------------------------------------------------------------------

    def GetName(self):

        return self._name

#---------------------------------------------------------------------------

    def GetPluginName(self):

        return self._plugin_data.GetName()

#---------------------------------------------------------------------------

    def GetType(self):

        return self._plugin_data.GetName()

#---------------------------------------------------------------------------

    def GetModuleName(self):

        return self._plugin_data.GetName()

#---------------------------------------------------------------------------

    def GetArguments(self):

        return self._arguments

#---------------------------------------------------------------------------

    def SetParameter(self, path, field, value):
        """!
        @brief Set's a parameter on the service
        """
        if self.verbose:

            print "\tModel Container: setting parameter %s %s %s" % (path, field, str(value))
        
        self._model_container.SetParameter(path, field, value)
        
#---------------------------------------------------------------------------

    def _ParseArguments(self):
        """!

        This currently parses arguments that are just an array
        with three entries, the third being the file to load
        like so:

            ['executable file', 'flags', 'filename']

        For this I'm assuming it's safe to simply load the third entry as the
        filename.
        """
        
        filename = ""

        if len(self._arguments) == 3:
            
            filename = self._arguments[-1]


        if self.verbose:

            print "Loading model from file '%s'" % filename

        
        self._model_container.Read(filename)
