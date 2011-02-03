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


class SSPy:


#---------------------------------------------------------------------------

    def __init__(self, verbose=False):

        self.verbose = verbose
        
        self._models = []

        self._schedulees = []

        # Internal schedule data to manage.
        self._schedule_data = {}
        self._schedule_file = ""

        # Registry objects for dynamically creating solvers and
        # other classes
        self._solver_registry = SolverRegistry()


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

    
    def _ParseSchedule(self, schedule_data):
        """
        @brief Parses the schedule 
        """
        
        
