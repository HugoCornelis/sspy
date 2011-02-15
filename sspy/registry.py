"""!
@file registry.py


This module contains classes used to dynamically create
solvers and objects from plugin specifications. Specific classes
present are:


    SolverRegistry: A registry used to create solver objects.
    ServiceRegistry: Registry used to create modeling service objects.
    OutputRegistry: Registry used to create output objects.
    InputRegistry: Registry used to create an input object.
    
"""
import errors
import imp
import os
import pdb
import sys
import yaml



#************************* Begin Registry ****************************
class Registry:
    """
    @class Registry A base class for creating a plugin registry

    
    """
#---------------------------------------------------------------------------

    def __init__(self, plugin_directory=None, plugin_file=None):

        self._plugin_directory = ""

        self._plugin_file = ""

        if plugin_directory is None:
#             curr_dir = os.path.dirname(os.path.abspath(__file__))

#             self._plugin_directory = os.path.join(curr_dir, "solvers")

#             if not os.path.isdir(self._plugin_directory):

            raise errors.PluginDirectoryError("No plugin directory specified")

        elif plugin_file is None:

            raise errors.PluginFileError("No plugin file identifier given")
        
        else:

            if os.path.isdir(plugin_directory):

                self._plugin_directory = plugin_directory

            else:

                raise errors.PluginDirectoryError("'%s' directory not found" % plugin_directory)


            self._plugin_file = plugin_file

        
        self._loaded_plugins = []

        plugins = self.GetPluginFiles()

        for p in plugins:

            self.LoadPlugin(p)


#---------------------------------------------------------------------------

    def LoadPlugin(self,plugin_file):

        if not os.path.exists(plugin_file):

            print "Error loading plugin, %s doesn't exist" % plugin_file
            
            return False

        try:

            plugin_entry = Plugin(plugin_file)

        except errors.PluginFileError, e:

            print "Error Loading Plugin %s, %s" % (plugin_file, e)

            return False

        if self.Exists(plugin_entry):

            raise errors.PluginError("Already a plugin with the name '%s'" % plugin_entry.GetName())

            return False

        else:
            
            self._loaded_plugins.append(plugin_entry)

            return True


#---------------------------------------------------------------------------

    def Exists(self, plugin):
        """
        @brief Determines if a plugin is present.
        """

        pi = self.GetPluginData(plugin.GetName())

        if pi is None:

            return False
        
        else:

            return True
        

#---------------------------------------------------------------------------

    def GetPluginData(self,name):

        for pi in self._loaded_plugins:

            if pi.GetName() == name:

                return pi

        return None
    
#---------------------------------------------------------------------------

    def GetPluginIndex(self,name):

        for index,pi in enumerate(self._loaded_plugins):

            if pi.GetName() == name:

                return index

        return -1
    

#---------------------------------------------------------------------------

    def GetPlugins(self):

        """!
        @brief Returns the list of solvers
        """
    
        return self._loaded_plugins

#---------------------------------------------------------------------------

    def GetEntries(self):
        """

        """
        return self.Gets()

#---------------------------------------------------------------------------

    def GetPluginFiles(self):

        """!
        @brief Returns the list of detected solver.
        """
        pis = self._FindPlugins()

        # exception?
    
        return pis

#---------------------------------------------------------------------------

    def _IsPlugin(self, path):
        """

        """
        return os.path.isfile( os.path.join( path, self._plugin_file ))

#---------------------------------------------------------------------------


    def _FindPlugins(self):
        """!
        @brief Finds all solvers plugin files in the solvers_dir

        Returns a list of the plugin files. 
        """

        plugins = []

        for path, directories, files in os.walk( self._plugin_directory ):
            if self._IsPlugin( path ):
                path.replace( '/','.' )

                pi = os.path.join(path, self._plugin_file)
            
                plugins.append(pi)

        return plugins



#*************************** End Registry ****************************





#************************ Begin Plugin ****************************

class Plugin:

    def __init__(self,yaml_file):
        """!

        """
        
        self._plugin_data = {}

        if os.path.exists(yaml_file):

            norm_file_path = os.path.normpath(yaml_file)

            try:
            
                self._plugin_data = yaml.load(open(norm_file_path,'rb'))
            
            except yaml.YAMLError, exc:    

                raise errors.PluginFileError("Failed to load simulation plugin %s: %s" % (p, exc))


            self._plugin_path = os.path.dirname(os.path.abspath(norm_file_path))

        else:

            raise errors.PluginFileError("Failed to load plugin %s" % yaml_file)


        self._file = ""

#---------------------------------------------------------------------------

    def __str__(self):

        return self.GetName()

#---------------------------------------------------------------------------

    def GetPath(self):

        return self._plugin_path
    

#---------------------------------------------------------------------------
    def GetName(self):

        if self._plugin_data.has_key('name'):

            return self._plugin_data['name']

        else:

            return "Unnamed"

#---------------------------------------------------------------------------

    def GetLabel(self):

        if self._plugin_data.has_key('label'):

            return self._plugin_data['label']

        else:

            return "No label specified"


#---------------------------------------------------------------------------
    def GetVersion(self):

        if self._plugin_data.has_key('version'):

            return self._plugin_data['version']

        else:

            return "No version given"


#---------------------------------------------------------------------------
    def GetDescription(self):

        if self._plugin_data.has_key('description'):

            return self._plugin_data['description']

        else:

            return "No description given"

#---------------------------------------------------------------------------

    def GetFile(self):

        if self._file != "":

            return self._file
        
        if self._plugin_data.has_key('file'):

            path = self.GetPath()
            
            my_file = self._plugin_data['file']

            self._file = path + "/" + my_file

            return self._file

        else:

            return ""


#---------------------------------------------------------------------------

    def GetModule(self):

        if self._plugin_data.has_key('module'):

            return self._plugin_data['module']

        elif self._plugin_data.has_key('file'):
                
                mod_name,file_ext = os.path.splitext(os.path.split(self._plugin_data['file'])[-1])

                return mod_name
            
        else:
            
            return ""
                

#***************************** End Plugin *****************************




#************************* Begin SolverRegistry ****************************

class SolverRegistry(Registry):
    """
    @class SolverRegistry A registry for the solver objects
    """
    
    def __init__(self, solver_directory):

        Registry.__init__(self,
                          plugin_directory=solver_directory,
                          plugin_file="solver.yml")

        
#---------------------------------------------------------------------------

    def CreateSolver(self, name, type=None, initializers=None, index=-1):

        plugin = None

        if type is not None:

            plugin = self.GetPluginData(type)

        elif index != -1:

            # bounds check?
            plugin = self._loaded_plugins[index]
            
        
        # First we check to see if we have the proper data to
        # allocate from a file.
        try:
            
            plugin_file = plugin.GetFile()

        except AttributeError:

            raise errors.ScheduleError("Cannot create Solver, invalid solver type '%s' for solver '%s'" % (type,name))
        
        if plugin_file != "":
            
            solver = self._InstantiateFromFile(plugin_file, name, initializers)

        return solver
    
#---------------------------------------------------------------------------

    def _InstantiateFromFile(self, filepath, name="Untitled", initializers=None):
        """
        @brief Creates a solver object from a plugin
        """
        class_inst = None
        expected_class = 'Solver'

        if not os.path.exists(filepath):

            raise errors.ScheduleError("Error: no such plugin to load class from: %s" % filepath)

        mod_name,file_ext = os.path.splitext(os.path.split(filepath)[-1])
        if file_ext.lower() == '.py':
            py_mod = imp.load_source(mod_name, filepath)

        elif file_ext.lower() == '.pyc':
            py_mod = imp.load_compiled(mod_name, filepath)
#        pdb.set_trace()
        if expected_class in dir(py_mod):

            try:

                class_inst = py_mod.Solver(name=name,
                                           constructor_settings=initializers) 

            except TypeError:

                raise errors.SolverError("'Solver' class is not found for plugin %s" % name)

        return class_inst

#---------------------------------------------------------------------------


#************************ End SolverRegistry **************************





#************************* Begin ServiceRegistry ****************************
class ServiceRegistry(Registry):

    def __init__(self, service_directory):

        Registry.__init__(self,
                          plugin_directory=service_directory,
                          plugin_file="service.yml")




#---------------------------------------------------------------------------

    def CreateService(self, name, type=None, index=-1):

        plugin_type = None

        if type is not None:

            plugin_type = self.GetPluginData(type)

        elif index != -1:

            # bounds check?
            plugin_type = self._service_plugins[index]
            
        
        # First we check to see if we have the proper data to
        # allocate from a file.
        try:
            
            plugin_file = plugin_type.GetFile()

        except AttributeError:

            raise errors.ScheduleError("Cannot create Service, invalid service type '%s' for service '%s'" % (type,name))
        
        if plugin_file != "":
            
            service = self._InstantiateFromFile(plugin_file,name)

        # verify sim legit?

        return service    


#---------------------------------------------------------------------------


    def _InstantiateFromFile(self, filepath, name="Untitled", constructor_settings=None):
        """

        """
        class_inst = None
        expected_class = 'Service'

        if not os.path.exists(filepath):

            raise errors.ServiceError("no such plugin to load class from: %s" % filepath)
        
            return None

        mod_name,file_ext = os.path.splitext(os.path.split(filepath)[-1])
        if file_ext.lower() == '.py':
            py_mod = imp.load_source(mod_name, filepath)

        elif file_ext.lower() == '.pyc':
            py_mod = imp.load_compiled(mod_name, filepath)
#        pdb.set_trace()
        if expected_class in dir(py_mod):

            try:

                class_inst = py_mod.Service(name=name, initializers=None) 

            except TypeError:

                raise errors.ServiceError("'Service' class is not found for plugin %s" % name)

        return class_inst

#---------------------------------------------------------------------------
#************************* End ServiceRegistry ****************************






#************************* Begin OutputRegistry ****************************
class OutputRegistry(Registry):
    """

    """
    
    def __init__(self, output_directory):

        Registry.__init__(self,
                          plugin_directory=output_directory,
                          plugin_file="output.yml")




#---------------------------------------------------------------------------

    def CreateOutput(self, name, type=None, index=-1):

        plugin_type = None

        if type is not None:

            plugin_type = self.GetPluginData(type)

        elif index != -1:

            # bounds check?
            plugin_type = self._output_plugins[index]
            
        
        # First we check to see if we have the proper data to
        # allocate from a file.
        try:
            
            plugin_file = plugin_type.GetFile()

        except AttributeError:

            raise errors.ScheduleError("Cannot create Output, invalid output type '%s' for output '%s'" % (type,name))
        
        if plugin_file != "":
            
            output = self._InstantiateFromFile(plugin_file,name)

        # verify sim legit?

        return output    


#---------------------------------------------------------------------------


    def _InstantiateFromFile(self, filepath, name="Untitled", constructor_settings=None):
        """

        """
        class_inst = None
        expected_class = 'Output'

        if not os.path.exists(filepath):

            raise errors.OutputError("no such plugin to load class from: %s" % filepath)
        
            return None

        mod_name,file_ext = os.path.splitext(os.path.split(filepath)[-1])
        if file_ext.lower() == '.py':
            py_mod = imp.load_source(mod_name, filepath)

        elif file_ext.lower() == '.pyc':
            py_mod = imp.load_compiled(mod_name, filepath)
#        pdb.set_trace()
        if expected_class in dir(py_mod):

            try:

                class_inst = py_mod.Output(name=name, initializers=None) 

            except TypeError:

                raise errors.OutputError("'Output' class is not found for plugin %s" % name)

        return class_inst

#---------------------------------------------------------------------------


#************************* End OutputRegistry ****************************







#************************* Begin InputRegistry ****************************
class InputRegistry(Registry):
    """

    """
    
    def __init__(self, input_directory):

        Registry.__init__(self,
                          plugin_directory=input_directory,
                          plugin_file="input.yml")




#---------------------------------------------------------------------------

    def CreateInput(self, name, type=None, index=-1):

        plugin_type = None

        if type is not None:

            plugin_type = self.GetPluginData(type)

        elif index != -1:

            # bounds check?
            plugin_type = self._input_plugins[index]
            
        
        # First we check to see if we have the proper data to
        # allocate from a file.
        try:
            
            plugin_file = plugin_type.GetFile()

        except AttributeError:

            raise errors.ScheduleError("Cannot create Input, invalid input type '%s' for input '%s'" % (type,name))
        
        if plugin_file != "":
            
            input_object = self._InstantiateFromFile(plugin_file,name)

        # verify sim legit?

        return input_object    


#---------------------------------------------------------------------------


    def _InstantiateFromFile(self, filepath, name="Untitled", constructor_settings=None):
        """

        """
        class_inst = None
        expected_class = 'Input'

        if not os.path.exists(filepath):

            raise errors.InputError("no such plugin to load class from: %s" % filepath)
        
            return None

        mod_name,file_ext = os.path.splitext(os.path.split(filepath)[-1])
        if file_ext.lower() == '.py':
            py_mod = imp.load_source(mod_name, filepath)

        elif file_ext.lower() == '.pyc':
            py_mod = imp.load_compiled(mod_name, filepath)
#        pdb.set_trace()
        if expected_class in dir(py_mod):

            try:

                class_inst = py_mod.Input(name=name, initializers=None) 

            except TypeError:

                raise errors.InputError("'Input' class is not found for plugin %s" % name)

        return class_inst

#---------------------------------------------------------------------------


#************************* End InputRegistry ****************************
