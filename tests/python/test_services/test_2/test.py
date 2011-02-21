


#*************************** Begin  Service ********************************

class Service:

#---------------------------------------------------------------------------

    def __init__(self, name=None, plugin_name=None, arguments=None, verbose=False):
        """

        """
        
        self._name = name

        self._module_name = ""


        if arguments is not None:

            pass

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

#******************************* End Service ********************************
