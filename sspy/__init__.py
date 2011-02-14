"""!
@package sspy

The simple scheduler in python is a software package that 
uses the model container and heccer solver to run a simulation 
with a set of simulation parameters. It can be extended by using 
plugins for solvers and simulation objects.

"""
import os
import pdb
import sys

try:
    import yaml
except ImportError:
    sys.exit("Need PyYaml http://pyyaml.org/\n")


from registry import SolverRegistry
from registry import ServiceRegistry









#*********************************** Begin SSPy ****************************
class SSPy:


#---------------------------------------------------------------------------

    def __init__(self, name="Untitled", verbose=False,
                 solver_directory= os.path.join( os.path.dirname(os.path.abspath(__file__)), 'plugins/solvers' ),
                 service_directory= os.path.join( os.path.dirname(os.path.abspath(__file__)), 'plugins/services' ),
                 input_directory= os.path.join( os.path.dirname(os.path.abspath(__file__)), 'plugins/inputs' ),
                 output_directory= os.path.join( os.path.dirname(os.path.abspath(__file__)), 'plugins/outputs' )
                 ):

        self.verbose = verbose

        self.name = name

        self._loaded_services = []
        
        self._models = []

        # arrays of schedulees to process when run.
        self._schedulees = []

        # Internal schedule data to manage.
        self._schedule_data = {}
        self._schedule_file = ""

        # Registry objects for dynamically creating solvers and
        # other classes
        self._solver_registry = SolverRegistry(solver_directory)
        
        self._service_registry = ServiceRegistry(service_directory)

#---------------------------------------------------------------------------


    def __del__(self):

        pass


#---------------------------------------------------------------------------

    def Load(self, filename):
        """
        @brief Loads a yaml specification
        """
        if os.path.exists(filename):

            norm_file_path = os.path.normpath(filename)

            try:
                
                self._schedule_data = yaml.load(open(norm_file_path,'rb'))
            
            except yaml.YAMLError, exc:    

                raise errors.ScheduleError("Failed to load schedule '%s' from file: %s" % (filename, exc))

        else:

            raise errors.ScheduleError("Schedule file '%s' doesn't exist" % filename)

        self._schedule_file = norm_file_path

        self.ParseSchedule(self._schedule_data)
        
#---------------------------------------------------------------------------

    def Dump(self):
        """

        """
        
        try:

            data = yaml.dump(self._schedule_data,
                             allow_unicode=True)

#                       encoding=encoding,
        except yaml.YAMLError, e:

            print "Error dumping schedule data: %s" % e


        if self.verbose:

            print "Dumping schedule data for %s\n" % self._schedule_file
            
        print data

#---------------------------------------------------------------------------

    def AddSchedulee(self, schedulee):
        """
        @brief Adds jobs to be scheduled.

        Adds input, output and solver objects to be scheduled.
        """

        # error checking?
        self._schedulees.append(schedulee)

#---------------------------------------------------------------------------

    def GetLoadedServices(self):

        return self._loaded_services

#---------------------------------------------------------------------------

    def GetSchedulees(self):

        return self._schedulees

#---------------------------------------------------------------------------

    def SetVerbose(self, verbose):

        self.verbose = verbose

#---------------------------------------------------------------------------

    def Advance(self):

        pass

#---------------------------------------------------------------------------

    def Compile(self):

        pass

#---------------------------------------------------------------------------
    
    def Analyze(self):

        pass

#---------------------------------------------------------------------------

    def ApplyRuntimeParameters(self):

        pass

#---------------------------------------------------------------------------

    def Connect(self):

        pass


#---------------------------------------------------------------------------
    def Daemonize(self):

        pass

#---------------------------------------------------------------------------

    def Finish(self):

        pass

#---------------------------------------------------------------------------

    def GetEngineOutputs(self):

        pass

#---------------------------------------------------------------------------

    def GetTimeStep(self):

        pass


#---------------------------------------------------------------------------

    def Help(self):

        pass

#---------------------------------------------------------------------------

    def History(self):

        pass

#---------------------------------------------------------------------------

    def Initiate(self):


        pass
   
#---------------------------------------------------------------------------

    def InstantiateCommunicators(self):

        pass
#---------------------------------------------------------------------------

    def InstantiateInputs(self):

        pass
#---------------------------------------------------------------------------

    def InstantiateOutputs(self):

        pass
#---------------------------------------------------------------------------

    def InstantiateServices(self):

        pass

#---------------------------------------------------------------------------

    def LookupModel(self):

        pass

#---------------------------------------------------------------------------

    def LookupObject(self):

        pass

#---------------------------------------------------------------------------
    def LookupSolverEngine(self):

        pass

#---------------------------------------------------------------------------
    def New(self):

        pass

#---------------------------------------------------------------------------
    def Optimize(self):

        pass

#---------------------------------------------------------------------------
    def Pause(self):

        pass

#---------------------------------------------------------------------------
    def Reconstruct(self):

        pass

#---------------------------------------------------------------------------
    def RegisterDriver(self):

        pass

#---------------------------------------------------------------------------
    def Run(self):

        pass

#---------------------------------------------------------------------------
    def Salvage(self):

        pass

#---------------------------------------------------------------------------
    def Save(self):

        pass

#---------------------------------------------------------------------------
    def ServiceRegister(self):

        pass

#---------------------------------------------------------------------------
    def Shell(self):

        pass

#---------------------------------------------------------------------------
    def Steps(self):

        pass

#---------------------------------------------------------------------------

    def Version(self):
        """

        """
        from __cbi__ import GetVersion

        return GetVersion()


#---------------------------------------------------------------------------
    
    def ParseSchedule(self, schedule_data):
        """
        @brief Parses the schedule

        Method parses the schedule data read in and creates
        a simulation based on the specification read in. The parse
        order follows the user workflow.

        
        Parse out the following top level keys to pass to helper methods:
            analyzers
            application_classes
            apply
            inputs
            input_classes
            models
            name
            optimize
            outputclasses
            outputs
            services
            solverclasses 
        """

        if self.verbose:

            print "Parsing schedule data"
        

        # Finds internal identifier for the schedule.
        if self._schedule_data.has_key('name'):

            self.name = self._schedule_data['name']

            if self.verbose:

                print "Schdule name is '%s'\n" % self.name

        # Loads the appropriate services for loading a model
        #   Such as the model_container
        if self._schedule_data.has_key('services'):

            services = self._schedule_data['services']

            if self.verbose:

                print "Found services:\n\t%s\n" % str(services)

            self._ParseServices(services)

        # This Loads the default options for registered solvers
        # along with the service that it requires. In the case
        # of Heccer, the default required service is the model
        # container.
        if self._schedule_data.has_key('solverclasses'):

            solvers = self._schedule_data['solverclasses']

            if self.verbose:

                print "Found Solver Classes:\n\t%s\n" % str(solvers)


            self._ParseSolvers(solvers)
            

        # This retrieves the model identifier from the model that
        # was loaded via services and the type of solver to use.
        # for instance if the root identifier of the loaded model is
        # called "/soma" then this is the modelname and the solver is set
        # to look for this symbol.
        if self._schedule_data.has_key('models'):

            models = self._schedule_data['models']


            if self.verbose:

                print "Found Models:\n\t%s\n" % str(models)
            


        # 
        if self._schedule_data.has_key('application_classes'):

            application_classes = self._schedule_data['application_classes']


            if self.verbose:

                print "Found Application Classes:\n\t%s\n" % str(application_classes)

       # Set of options for configuring analyzers
        if self._schedule_data.has_key('analyzers'):
            
            analyzers = self._schedule_data['analyzers']
            
            if self.verbose:

                print "Found analyzers to apply:\n\t%s\n" % str(analyzers)
            

        # Set of options that define how to run this schedule.
        if self._schedule_data.has_key('apply'):
            
            apply_parameters = self._schedule_data['apply']
            
            if self.verbose:

                print "Found Simulation Parameters to apply:\n\t%s\n" % str(apply_parameters)
            



        # Here we parse for external simulation objects that generate input into
        # the model. 
        if self._schedule_data.has_key('inputclasses'):

            inputclasses = self._schedule_data['inputclasses']


            if self.verbose:

                print "Found Input Classes:\n\t%s" % str(inputclasses)
            

            # Key contains the attributes for the inputclass objects that
            # were loaded.
            if self._schedule_data.has_key('inputs'):

                inputs = self._schedule_data['inputs']

                if self.verbose:

                    print "\tFound Inputs: %s\n" % str(inputs)
            

                
        # Specifies the output objects to use.
        if self._schedule_data.has_key('outputclasses'):

            outputclasses = self._schedule_data['solverclasses']

            if self.verbose:

                print "Found Output Classes:\n\t%s" % str(outputclasses)

            # Attributes for the outputclass objects that were loaded.
            if self._schedule_data.has_key('outputs'):
                
                outputs = self._schedule_data['outputs']

                if self.verbose:

                    print "\tFound Outputs: %s\n" % str(outputs)

#---------------------------------------------------------------------------


    def _ParseSolvers(self, solver_data):
        """!
        @brief Loads solvers from schedule data

        Processes a dictionary that was parsed from a schedule
        in YAML
        """

        try:

            items = solver_data.items()

        except AttributeError, e:

            raise errors.ScheduleError("Error parsing solvers, %s" % e)


        for solver_type, data in solver_data.iteritems():

            solver_name = ""
            
            if data.has_key('name'):

                solver_name = data['name']

            else:
                
                solver_name = "%s (%s)" % (self.name, solver_type)


            if self.verbose:

                print "Loading Solver '%s' of type '%s'" % (solver_name, solver_type)

#            pdb.set_trace()
            solver = self._solver_registry.CreateSolver(solver_name, solver_type, solver_data)

            self.AddSchedulee(solver)

#---------------------------------------------------------------------------

    def _ParseServices(self, service_data):
        """!
        @brief Loads services from schedule data

        Processes a dictionary that was parsed from a schedule
        in YAML
        """

        try:

            items = service_data.items()

        except AttributeError, e:

            raise errors.ScheduleError("Error parsing services, %s" % e)


        for service_type, data in service_data.iteritems():

            service_name = ""
            
            if data.has_key('name'):

                service_name = data['name']

            else:
                
                service_name = "%s (%s)" % (self.name, service_type)

            service = self._service_registry.CreateService(service_name, service_type, service_data)

            if self.verbose:

                print "Loading service '%s' of type '%s'" % (service_name, service_type)
            
            self._loaded_services.append(service)
            
#---------------------------------------------------------------------------

    def _ParseOutputs(self, output_data, output_parameters):
        """
        @brief Loads outputs from python dictionaries.
        """


        try:

            items = output_data.items()

            items = output_parameters.items()
            
        except AttributeError, e:

            raise errors.ScheduleError("Error parsing services, %s" % e)

        
#---------------------------------------------------------------------------        

    def _ParseInputs(self, input_data, input_parameters):
        """

        """


        try:

            items = service_data.items()

        except AttributeError, e:

            raise errors.ScheduleError("Error parsing services, %s" % e)
        
#*********************************** End SSPy *******************************
