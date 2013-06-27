"""!
@file registry.py


This module contains classes used to dynamically create
solvers and objects from plugin specifications. Specific classes
present are:


    SolverRegistry: A registry used to create solver objects.
    ServiceRegistry: Registry used to create modeling service objects.
    OutputRegistry: Registry used to create output objects.
    InputRegistry: Registry used to create an input object.
    EventDistributorRegistry: Registry used to create an event distributor object.
    
"""
import errors
import imp
import os
import pdb
import sys
import yaml

from plugin import Plugin


#************************* Begin Registry ****************************
class Registry:
    """
    @class Registry A base class for creating a plugin registry

    
    """
#---------------------------------------------------------------------------

    def __init__(self, plugin_directory=None, plugin_file=None, verbose=False):

        self._plugin_directory = ""

        self._plugin_file = ""

        self.verbose = verbose
        
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

        
        self._loaded_plugins = {}

        plugins = self.GetPluginFiles()

        for p in plugins:

            self.LoadPlugin(p)


#---------------------------------------------------------------------------

    def Create(self, name, type, arguments=None):

        plugin = self.GetPluginData(type)

        return self._InstantiateFromFile(plugin, name, arguments)

#---------------------------------------------------------------------------

    def LoadPlugin(self, plugin_filename):

        if not os.path.exists(plugin_filename):

            print "Error loading plugin, %s doesn't exist" % plugin_filename
            
            return False

        try:

            plugin_entry = Plugin(plugin_filename)

        except errors.PluginFileError, e:

            print "Error Loading Plugin %s, %s" % (plugin_filename, e)

            return False

        if self._loaded_plugins.has_key(plugin_entry.GetName()):

            raise errors.PluginError("Already a plugin with the name '%s'" % plugin_entry.GetName())

            return False

        else:
            
            self._loaded_plugins[plugin_entry.GetName()] = plugin_entry

            return True


#---------------------------------------------------------------------------

    def GetPluginData(self,name):

        if self._loaded_plugins.has_key(name):

            return self._loaded_plugins[name]

        return None
    
#---------------------------------------------------------------------------

    def GetPlugins(self):

        """!
        @brief Returns the list of solvers
        """
    
        return self._loaded_plugins.values()

#---------------------------------------------------------------------------

    def GetPluginFiles(self):

        """!
        @brief Returns the list of detected plugins.
        """

        plugins = []

        for path, directories, files in os.walk( self._plugin_directory ):

            if os.path.isfile( os.path.join( path, self._plugin_file )):

                path.replace( '/','.' )

                pi = os.path.join(path, self._plugin_file)
            
                plugins.append(pi)

        return plugins


#---------------------------------------------------------------------------


    def _InstantiateFromFile(self, plugin, name="Untitled", arguments=None):
        """
        @brief Creates an instance from a plugin
        """
        class_inst = None
        expected_class = 'Instance'

        
        # First we check to see if we have the proper data to
        # allocate from a file.
        try:
            
            filepath = plugin.GetFile()

        except AttributeError, e:

            raise errors.ScheduleError("Cannot create %s, invalid plugin '%s', %s" % (plugin.GetName(), name, e))


        if not os.path.exists(filepath):

            raise errors.ScheduleError("Error: no such plugin to load class from: %s" % filepath)

        mod_name,file_ext = os.path.splitext(os.path.split(filepath)[-1])
        if file_ext.lower() == '.py':
            py_mod = imp.load_source(mod_name, filepath)

        elif file_ext.lower() == '.pyc':
            py_mod = imp.load_compiled(mod_name, filepath)

        if expected_class in dir(py_mod):

            
            try:
                
                class_inst = py_mod.Instance(name=name,
                                             plugin=plugin,
                                             arguments=arguments,
                                             verbose=self.verbose) 

            except Exception, e:

                raise errors.ScheduleError("'%s' class '%s' cannot be created: %s" % (plugin.GetName(), name, e))

        return class_inst


#---------------------------------------------------------------------------


#*************************** End Registry ****************************









#************************* Begin SolverRegistry ****************************

class SolverRegistry(Registry):
    """
    @class SolverRegistry A registry for the solver objects
    """
    
    def __init__(self, solver_directory, verbose=False):

        Registry.__init__(self,
                          plugin_directory=solver_directory,
                          plugin_file="solver.yml",
                          verbose=verbose)

        self.verbose = verbose
        
#************************ End SolverRegistry **************************





#************************* Begin ServiceRegistry ****************************
class ServiceRegistry(Registry):

    def __init__(self, service_directory, verbose=False):

        Registry.__init__(self,
                          plugin_directory=service_directory,
                          plugin_file="service.yml",
                          verbose=verbose)


#************************* End ServiceRegistry ****************************






#************************* Begin OutputRegistry ****************************
class OutputRegistry(Registry):
    """

    """
    
    def __init__(self, output_directory, verbose=False):

        Registry.__init__(self,
                          plugin_directory=output_directory,
                          plugin_file="output.yml",
                          verbose=verbose)


#************************* End OutputRegistry ****************************







#************************* Begin InputRegistry ****************************
class InputRegistry(Registry):
    """

    """

    def __init__(self, input_directory, verbose=False):

        Registry.__init__(self,
                          plugin_directory=input_directory,
                          plugin_file="input.yml",
                          verbose=verbose)


#************************* End InputRegistry ****************************







#************************* Begin EventDistributorRegistry ***************
class EventDistributorRegistry(Registry):
    """

    """

    def __init__(self, event_distributor_directory, verbose=False):

        Registry.__init__(self,
                          plugin_directory=event_distributor_directory,
                          plugin_file="event_distributor.yml",
                          verbose=verbose)


#---------------------------------------------------------------------------


#************************* End EventDistributorRegistry ****************************
