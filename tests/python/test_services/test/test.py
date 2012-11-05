


#*************************** Begin  Service ********************************

class Service:

#---------------------------------------------------------------------------

    def __init__(self, name=None, plugin=None, arguments=None, verbose=False):
        """

        """
        self._plugin_data = plugin
        
        self._name = name

        self._module_name = ""

        self._arguments = None

        if arguments is not None:

            pass

#---------------------------------------------------------------------------

    def GetObject(self):

        return None
    
#---------------------------------------------------------------------------

    def GetName(self):

        return self._name

#---------------------------------------------------------------------------

    def GetType(self):

        return self._plugin_data.GetName()

#---------------------------------------------------------------------------

    def GetType(self):

        return self._plugin_data.GetName()
    
#---------------------------------------------------------------------------

    def GetModuleName(self):

        return self._module_name

#---------------------------------------------------------------------------

    def GetArguments(self):

        return self._arguments

#******************************* End Service ********************************
