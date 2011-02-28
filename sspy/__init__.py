"""!
@package sspy

The simple scheduler in python is a software package that 
uses the model container and heccer solver to run a simulation 
with a set of simulation parameters. It can be extended by using 
plugins for solvers and simulation objects.

"""
import os
import pdb
import pprint
import sys

try:
    import yaml
except ImportError:
    sys.exit("Need PyYaml http://pyyaml.org/\n")


from registry import SolverRegistry
from registry import ServiceRegistry

from schedulee import Schedulee


#*********************************** Begin SSPy ****************************
class SSPy:


#---------------------------------------------------------------------------

    def __init__(self, name="Untitled", verbose=False,
                 solver_directory= os.path.join( os.path.dirname(os.path.abspath(__file__)), 'plugins/solvers' ),
                 service_directory= os.path.join( os.path.dirname(os.path.abspath(__file__)), 'plugins/services' ),
                 input_directory= os.path.join( os.path.dirname(os.path.abspath(__file__)), 'plugins/inputs' ),
                 output_directory= os.path.join( os.path.dirname(os.path.abspath(__file__)), 'plugins/outputs' )
                 ):

        # Registry objects for dynamically creating solvers and
        # other objects

        
        self.verbose = verbose

        # set up the pretty printer for printing out dicts and arrays
        self.pp = pprint.PrettyPrinter()

        # Create our registry services for solvers, services, inputs
        # and outputs
        self._solver_registry = SolverRegistry(solver_directory, verbose=self.verbose)
        self._service_registry = ServiceRegistry(service_directory, verbose=self.verbose)


        self.name = name

        self._analyzers = {}
            
        self._loaded_services = []

        self._solvers = []
        
        self._models = []

        self._compiled = False

        # Internal schedule data to manage.
        self._schedule_data = {}
        self._schedule_file = ""

        # arrays of schedulees to process when run.
        self._schedulees = []


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
        """
        @brief Compiles all solvers 
        """

        for solver in self._solvers:

            try:

                if self.verbose:

                    print "Compiling Solver: %s" % solver.GetName()
                    
                solver.Compile()

            except Exception, e:

                print "\tError compiling solver: %s" % e

        self._compiled = True

#---------------------------------------------------------------------------
    
    def Analyze(self):

        pass

#---------------------------------------------------------------------------

    def ApplyRuntimeParameters(self):

        pass

#---------------------------------------------------------------------------

    def Connect(self):
        """
        @brief Connects services to solvers

        
        """
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
        """
        @brief Method ensures that all needed keys are present
        @deprecated

        Most likely not needed since data from the specification is loaded
        into internal variables for processing and data manipulation instead
        of working off of the dictionary that is loaded straight from the file. 
        """
        pass

#---------------------------------------------------------------------------
    def Save(self):

        pass

#---------------------------------------------------------------------------

    def RegisterSchedulee(self, schedulee):

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

            self.name = schedule_data['name']

            if self.verbose:

                print "Schdule name is '%s'\n" % self.name

        # Loads the appropriate services for loading a model
        #   Such as the model_container
        if self._schedule_data.has_key('services'):

            services = schedule_data['services']

            self._ParseServices(services)

        # This Loads the default options for registered solvers
        # along with the service that it requires. In the case
        # of Heccer, the default required service is the model
        # container.
        if self._schedule_data.has_key('solverclasses'):

            solvers = schedule_data['solverclasses']


            self._ParseSolvers(solvers)
            

        # This retrieves the model identifier from the model that
        # was loaded via services and the type of solver to use.
        # for instance if the root identifier of the loaded model is
        # called "/soma" then this is the modelname and the solver is set
        # to look for this symbol.
        if self._schedule_data.has_key('models'):

            self._models = schedule_data['models']

        # 
        if self._schedule_data.has_key('application_classes'):

            application_classes = schedule_data['application_classes']

            self._ParseApplicationClasses(application_classes)


       # Set of options for configuring analyzers
        if self._schedule_data.has_key('analyzers'):
            
            self._analyzers = schedule_data['analyzers']
            
            

        # Set of options that define how to run this schedule.
        if self._schedule_data.has_key('apply'):
            
            apply_parameters = schedule_data['apply']

            self._ParseAppliedParameters(apply_parameters)


        # Here we parse for external simulation objects that generate input into
        # the model. 
        if self._schedule_data.has_key('inputclasses'):

            inputclasses = schedule_data['inputclasses']
            

            # Key contains the attributes for the inputclass objects that
            # were loaded.
            if self._schedule_data.has_key('inputs'):

                inputs = schedule_data['inputs']


        # Specifies the output objects to use.
        if self._schedule_data.has_key('outputclasses'):

            outputclasses = schedule_data['solverclasses']


            # Attributes for the outputclass objects that were loaded.
            if self._schedule_data.has_key('outputs'):
                
                outputs = schedule_data['outputs']


            self._ParseOutputs(outputclasses, outputs)


#---------------------------------------------------------------------------


    def _ParseApplicationClasses(self, application_class_data):

        if self.verbose:

            print "Found application classes:"
            
        if application_class_data.has_key('analyzers'):

            analyzers = application_class_data['analyzers']

            if self.verbose:
                
                print "\tApplication class: analyzers"


        if application_class_data.has_key('finishers'):

            finishers = application_class_data['finishers']

            if self.verbose:
                
                print "\tApplication class: finishers"

        if application_class_data.has_key('initializers'):

            initializers = application_class_data['initializers']

            if self.verbose:
                
                print "\tApplication class: initializers"

        if application_class_data.has_key('modifiers'):

            modifiers = application_class_data['modifiers']

            if self.verbose:
                
                print "\tApplication class: modifiers"

        if application_class_data.has_key('results'):

            results = application_class_data['results']

            if self.verbose:
                
                print "\tApplication class: results"

        if application_class_data.has_key('services'):

            services = application_class_data['services']

            if self.verbose:
                
                print "\tApplication class: services"

        if application_class_data.has_key('simulation'):

            simulation = application_class_data['simulation']

            if self.verbose:
                
                print "\tApplication class: simulation"

#---------------------------------------------------------------------------

    def _ParseAppliedParameters(self, apply_parameters):


        if self.verbose:

            print "\nFound applied simulation parameters:"

        if apply_parameters.has_key('simulation'):

            parameter_sets = apply_parameters['simulation']

            if self.verbose:

                print "Simulation set: "

                self.pp.pprint(parameter_sets)
                
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

            try:
                
                solver = self._solver_registry.CreateSolver(solver_name, solver_type, data)

            except Exception, e:

                raise errors.ScheduleError("Error, cannot create solver '%s' of type '%s', %s" % (solver_name, solver_type, e))

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

            service_initiaizers = None

            if data.has_key('initializers'):

                initializers = data['initializers']

                for i in initializers:

                    if i.has_key('arguments'):
                        
                        arguments = i['arguments']

                    else:

                        print "Error processing arguments for '%s' of type '%s'" % (service_name, service_type)

                    for arg in arguments:

                        try:
                        
                            service = self._service_registry.CreateService(service_name,
                                                                           service_type,
                                                                           arg)
                        
                        except Exception, e:

                            print "Error creating service. %s" % e

                            continue


                        if self.verbose:

                            print "Loading Service '%s' of type '%s'" % (service_name, service_type)
            
                        self._loaded_services.append(service)

            else:
                
                raise errors.ScheduleError("Error parsing services, no initializers key")
                


            
#---------------------------------------------------------------------------

    def _ParseOutputs(self, output_data, output_parameters=None):
        """
        @brief Loads outputs from python dictionaries.
        """


        try:

            items = output_data.items()

            items = output_parameters.items()
            
        except AttributeError, e:

            raise errors.ScheduleError("Error parsing services, %s" % e)


        for output_type, data in output_data.iteritems():

            output_name = ""
            
            if output_data.has_key('name'):

                output_name = data['name']

            else:
                
                output_name = "%s (%s)" % (self.name, output_type)


            if self.verbose:

                print "Loading Output '%s' of type '%s'" % (output_name, output_type)

#            pdb.set_trace()
            output = self._solver_registry.CreateOutput(output_name, output_type, output_parameters)

            self.AddSchedulee(output)



#---------------------------------------------------------------------------        

    def _ParseInputs(self, input_data, input_parameters):
        """

        """


        try:

            items = service_data.items()

        except AttributeError, e:

            raise errors.ScheduleError("Error parsing services, %s" % e)
        
#*********************************** End SSPy *******************************
