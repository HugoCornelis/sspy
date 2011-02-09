"""!
@file registry.py

@class SolverRegistry
@class SolverPlugin

This module contains classes used to dynamically create
solvers and objects from plugin specifications. 
"""
import errors
import imp
import os
import pdb
import sys
import yaml

#************************* Begin SolverRegistry ****************************
class SolverRegistry:
    """
    
    """

#---------------------------------------------------------------------------

    def __init__(self, solver_directory=None):

        self._solver_directory = ""

        if solver_directory is None:
            
            curr_dir = os.path.dirname(os.path.abspath(__file__))

            self._solver_directory = os.path.join(curr_dir, "solvers")

            if not os.path.isdir(self._solver_directory):
        
                raise errors.SolverError("'solvers' directory not found")
            
        else:

            if os.path.isdir(solver_directory):

                self._solver_directory = solver_directory

            else:

                raise errors.SolverError("'%s' directory not found" % solver_directory)
            
        
        self._solver_plugins = []

        plugins = self.GetPluginFiles()

        for p in plugins:

            self.LoadPlugin(p)

#---------------------------------------------------------------------------

    def CreateSolver(self, name, type=None, index=-1):

        plugin_type = None

        if type is not None:

            plugin_type = self.GetPluginData(type)

        elif index != -1:

            # bounds check?
            plugin_type = self._solver_plugins[index]
            
        
        # First we check to see if we have the proper data to
        # allocate from a file.
        try:
            
            plugin_file = plugin_type.GetFile()

        except AttributeError:

            raise errors.ScheduleError("Cannot create Solver, invalid solver type '%s' for solver '%s'" % (type,name))
        
        if plugin_file != "":
            
            solver = self._InstantiateFromFile(plugin_file,name)

        # verify sim legit?

        return solver        

#---------------------------------------------------------------------------

    def LoadPlugin(self,solver_file):

        if not os.path.exists(solver_file):

            print "Error loading plugin, %s doesn't exist" % solver_file
            
            return False

        try:

            solver_entry = SolverPlugin(solver_file)

        except errors.SolverError, e:

            print "Error Loading Plugin %s, %s" % (solver_file, e)

            return False

        if self.Exists(solver_entry):

            raise errors.SolverError("Already a solver plugin with the name '%s'" % solver_entry.GetName())

            return False

        else:
            
            self._solver_plugins.append(solver_entry)

            return True


#---------------------------------------------------------------------------

    def Exists(self, solver_plugin):
        """
        @brief 
        """

        sp = self.GetPluginData(solver_plugin.GetName())

        if sp is None:

            return False
        
        else:

            return True
        

#---------------------------------------------------------------------------

    def GetPluginData(self,name):

        for sp in self._solver_plugins:

            if sp.GetName() == name:

                return sp

        return None
    
#---------------------------------------------------------------------------

    def GetPluginIndex(self,name):

        for index,sp in enumerate(self._simulator_plugins):

            if sp.GetName() == name:

                return index

        return -1
    

#---------------------------------------------------------------------------

    def GetPlugins(self):

        """!
        @brief Returns the list of solvers
        """
    
        return self._solver_plugins

#---------------------------------------------------------------------------

    def GetEntries(self):
        """

        """
        return self.GetSolvers()

#---------------------------------------------------------------------------

    def GetPluginFiles(self):

        """!
        @brief Returns the list of detected solver.
        """
        pis = self._FindSolverPlugins()

        # exception?
    
        return pis

#---------------------------------------------------------------------------

    def _IsSolver(self, path):
        """

        """
        return os.path.isfile( os.path.join( path, 'solver.yml' ))

#---------------------------------------------------------------------------


    def _FindSolverPlugins(self):
        """!
        @brief Finds all solvers plugin files in the solvers_dir

        Returns a list of the plugin files. 
        """

        plugins = []

        for path, directories, files in os.walk( self._solver_directory ):
            if self._IsSolver( path ):
                path.replace( '/','.' )

                pi = path + "/solver.yml"
            
                plugins.append(pi)

        return plugins


#---------------------------------------------------------------------------

    def _FindSolvers(self):
        """!
        @brief Finds all solvers in the solvers_dir

        Returns a list of the solver directories 
        """

        solvers = []

        for path, directories, files in os.walk( self._solver_directory ):
            if self._IsSolver( path ):
                path.replace( '/','.' )
                
                solvers.append(path)

        return solvers

#---------------------------------------------------------------------------

    def _InstantiateFromFile(self,filepath,name="Untitled", constructor_settings=None):
        """

        """
        class_inst = None
        expected_class = 'Solver'

        if not os.path.exists(filepath):
            # Exception?
            print "Error: no such plugin to load class from: %s" % filepath
            return None

        mod_name,file_ext = os.path.splitext(os.path.split(filepath)[-1])
        if file_ext.lower() == '.py':
            py_mod = imp.load_source(mod_name, filepath)

        elif file_ext.lower() == '.pyc':
            py_mod = imp.load_compiled(mod_name, filepath)
#        pdb.set_trace()
        if expected_class in dir(py_mod):

            try:

                class_inst = py_mod.Solver(name=name, constructor_settings=None) 

            except TypeError:

                raise errors.SolverError("'Solver' class is not found for plugin %s" % name)

        return class_inst

#---------------------------------------------------------------------------

#*************************** End SolverRegistry ****************************





#************************ Begin SolverPlugin ****************************

class SolverPlugin:

    def __init__(self,yaml_file):
        """!

        """
        
        self._plugin_data = {}

        if os.path.exists(yaml_file):

            norm_file_path = os.path.normpath(yaml_file)

            try:
            
                self._plugin_data = yaml.load(open(norm_file_path,'rb'))
            
            except yaml.YAMLError, exc:    

                raise errors.SolverError("Failed to load simulation plugin %s: %s" % (p, exc))


            self._plugin_path = os.path.dirname(os.path.abspath(norm_file_path))

        else:

            raise errors.SolverError("Failed to load plugin %s" % yaml_file)


        self._file = ""


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
                

#***************************** End SolverPlugin *****************************






#************************* Begin ServiceRegistry ****************************
class ServiceRegistry:
    """
    
    """

#---------------------------------------------------------------------------

    def __init__(self, service_directory=None):

        self._service_directory = ""

        if service_directory is None:
            
            curr_dir = os.path.dirname(os.path.abspath(__file__))

            self._service_directory = os.path.join(curr_dir, "services")

            if not os.path.isdir(self._service_directory):
        
                raise errors.ServiceError("'services' directory not found")
            
        else:

            if os.path.isdir(service_directory):

                self._service_directory = service_directory

            else:

                raise errors.ServiceError("'%s' directory not found" % service_directory)
            
        
        self._service_plugins = []

        plugins = self.GetPluginFiles()

        for p in plugins:

            self.LoadPlugin(p)

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

    def LoadPlugin(self, service_file):

        if not os.path.exists(service_file):

            print "Error loading plugin, %s doesn't exist" % service_file
            
            return False

        try:

            service_entry = ServicePlugin(service_file)

        except errors.ServiceError, e:

            print "Error Loading Plugin %s, %s" % (service_file, e)

            return False

        if self.Exists(service_entry):

            raise errors.ServiceError("Already a service plugin with the name '%s'" % service_entry.GetName())

            return False

        else:
            
            self._service_plugins.append(service_entry)

            return True


#---------------------------------------------------------------------------

    def Exists(self, service_plugin):
        """
        @brief 
        """

        sp = self.GetPluginData(service_plugin.GetName())

        if sp is None:

            return False
        
        else:

            return True
        

#---------------------------------------------------------------------------

    def GetPluginData(self,name):

        for sp in self._service_plugins:

            if sp.GetName() == name:

                return sp

        return None
    
#---------------------------------------------------------------------------

    def GetPluginIndex(self,name):

        for index,sp in enumerate(self._simulator_plugins):

            if sp.GetName() == name:

                return index

        return -1
    

#---------------------------------------------------------------------------

    def GetPlugins(self):

        """!
        @brief Returns the list of services
        """
    
        return self._service_plugins

#---------------------------------------------------------------------------

    def GetEntries(self):
        """

        """
        return self.GetServices()

#---------------------------------------------------------------------------

    def GetPluginFiles(self):

        """!
        @brief Returns the list of detected service.
        """
        pis = self._FindServicePlugins()

        # exception?
    
        return pis

#---------------------------------------------------------------------------

    def _IsService(self, path):
        """

        """
        return os.path.isfile( os.path.join( path, 'service.yml' ))

#---------------------------------------------------------------------------


    def _FindServicePlugins(self):
        """!
        @brief Finds all services plugin files in the services_dir

        Returns a list of the plugin files. 
        """

        plugins = []

        for path, directories, files in os.walk( self._service_directory ):
            if self._IsService( path ):
                path.replace( '/','.' )

                pi = path + "/service.yml"
            
                plugins.append(pi)

        return plugins


#---------------------------------------------------------------------------

    def _FindServices(self):
        """!
        @brief Finds all services in the services_dir

        Returns a list of the service directories 
        """

        services = []

        for path, directories, files in os.walk( self._service_directory ):
            if self._IsService( path ):
                path.replace( '/','.' )
                
                services.append(path)

        return services

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

#*************************** End ServiceRegistry ****************************





#************************ Begin ServicePlugin ****************************

class ServicePlugin:

    def __init__(self,yaml_file):
        """!

        """
        
        self._plugin_data = {}

        if os.path.exists(yaml_file):

            norm_file_path = os.path.normpath(yaml_file)

            try:
            
                self._plugin_data = yaml.load(open(norm_file_path,'rb'))
            
            except yaml.YAMLError, exc:    

                raise errors.ServiceError("Failed to load simulation plugin %s: %s" % (p, exc))


            self._plugin_path = os.path.dirname(os.path.abspath(norm_file_path))

        else:

            raise errors.ServiceError("Failed to load plugin %s" % yaml_file)


        self._file = ""


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
                

#***************************** End ServicePlugin *****************************
