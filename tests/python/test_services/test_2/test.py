


#*************************** Begin  Service ********************************

class Service:

#---------------------------------------------------------------------------

    def __init__(self, name=None, initializers=None, verbose=False):
        """

        """
        
        self._name = name

        self._module_name = ""

        self._arguments = None

        if initializers is not None:

            if initializers.has_key('module_name'):

                self._module_name = initializers['module_name']

            if initializers.has_key('arguments'):

                self._arguments = initializers['arguments']

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
