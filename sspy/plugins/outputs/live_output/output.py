"""
This is the output plugin for outputting data
from connected solvers into a live data structure
"""
import os
import pdb
import sys

try:

    from experiment.output import LiveOutput

except ImportError, e:

    sys.exit("Error importing the Live Output object: %s\n" % e)



class Instance:

#---------------------------------------------------------------------------

    def __init__(self,  name="Untitled Output", plugin=None,
                 arguments=None, verbose=False):

        self._name = name

        self._plugin_data = plugin

        self.verbose = verbose


        # should be inconsequential in an output object
        # it is only here for reporting purposes to keep
        # the object consistent when it's passed on to
        # the schedulee.
        self.time_step = 0.0
        
        self._live_output = None

        self.mode = None

        self.resolution = None
        
        self.outputs = []

        self.outputs_parsed = False

        self.append = False

        self.order = "row"

        self._solver_collection = None

        if not arguments is None:
            
            self._ParseArguments(arguments)

            

#---------------------------------------------------------------------------

    def Compile(self):
        """
        @brief 
        """
        self._live_output.Compile()

#---------------------------------------------------------------------------

    def Finish(self):
        """
        @brief 
        """
        self._live_output.Finish()

#---------------------------------------------------------------------------

    def GetName(self):
        """
        @brief 
        """
        return self._name

#---------------------------------------------------------------------------

    def Name(self):

        return self._name

#---------------------------------------------------------------------------

    def SetOutputs(self, outputs):
        """
        @brief Sets the list of outputs

        Needs to be saved for later since they cannot be set
        until the solver is created after a connect. 
        """
        
        self.outputs = outputs

#---------------------------------------------------------------------------

    def AddOutput(self, name, field):
        """!

        @brief Adds an output to the solver


        Performs a check for the solver type. Any issues after the solver check
        should throw an exception. 
        """

        if self._solver_collection is None:
            # if it's none then we store it for later use

            self.outputs.append(dict(field=field,component_name=name))
            

        else:

            self.AddAddressFromSolver(name, field)

            self.outputs.append(dict(field=field,component_name=name))
            
#---------------------------------------------------------------------------

    def AddAddressFromSolver(self, name, field, solver=None):
        """

        """
            
        if self._solver_collection is None:

            raise Exception("Output error: can't add output for %s, %s: No Solvers connected" % (name, field))
        
        try:

            address = self._solver_collection.GetAddress(name, field, solver)

            # here the name and address gets passed to the lower level object
            
            self._live_output.AddOutput(name, address)
    
        except Exception, e:
                
            raise Exception("Output error: can't add output for %s, %s: %s" % (name, field, e))

#---------------------------------------------------------------------------

    def GetTimeStep(self):
        """
        """
        
        return self.time_step

#---------------------------------------------------------------------------

    def SetTimeStep(self, time_step):
        """
        """
        
        self.time_step = time_step

#---------------------------------------------------------------------------
    

    def GetType(self):

        return self._plugin_data.GetName()

#---------------------------------------------------------------------------

    def Finish(self):

        self._live_output.Finish()

#---------------------------------------------------------------------------

    def Initialize(self):

        # if the output object is not built declaratively
        # then it must be built here just before connection to a solver. 
        if self._live_output is None:

            self._live_output = LiveOutput()

            if self._live_output is None:

                raise Exception("Can't create output generator object '%s'" % self.GetName())

        # Here we set any output parameters we loaded into the plugin

        if not self.mode is None:
            
            if self.mode == 'steps':
                        
                self._live_output.SetSteps(1)


        if not self.resolution is None:

            self._live_output.SetResolution(self.resolution)


        self._live_output.SetOrder(self.order)

#---------------------------------------------------------------------------

    def Reset(self):
        """!
        @brief Destroys and recreates the core output object
        """

        if not self.append:

            self.Finish()

            self._live_output = None
            
            # if we destroy the object we need to flag it as not loaded
            # so we can reload them after reconnecting. The plugin is still
            # connected because we have an internal copy of the solver
            self.outputs_parsed = False

        self.Initialize()

        self._ParseOutputs()
            
#---------------------------------------------------------------------------

    def Connect(self, solvers):
        """!
        @brief Connects the output to a solver

        To properly connect a solver and an output you must:

            1. Retrieve the timestep from the solver and set it
            with the SetTimeStep method to ensure the scheudlee
            properly updates the object.

            2. Connect the solver core to the output core.

            3. Add the outputs via whatever method the cores use
            to communicate.

        """

        # Here we save a copy of the solver
        # in case we don't set any outputs during connection
        # but with to set them later (via shell)
        self._solver_collection = solvers
        

        # initialize the object at this point
        self.Initialize()


        # Here we need to get the timestep and set it
        # for our object
        time_step = self._solver_collection.GetTimeStep()
            
        self.SetTimeStep(time_step)

        # Now after connection we can add any stored
        # outputs from a configuration. Otherwise
        # they can only be added after this connection step
        # has proceeded. 
        self._ParseOutputs()


#---------------------------------------------------------------------------


    def Step(self, time=None):
        """

        """
        self._live_output.Step(time)


#---------------------------------------------------------------------------

    def Report(self):

        pass

#---------------------------------------------------------------------------

    def SetMode(self, mode=None):
        """

        """
            
        self.mode = mode

#---------------------------------------------------------------------------

    def SetResolution(self, res=None):
        """

        """
        self.resolution = res

#---------------------------------------------------------------------------

    def SetAppend(self, append=False):

        self.append = append

#---------------------------------------------------------------------------

    def SetOrder(self, order):

        self.order = order

#---------------------------------------------------------------------------

    def GetData(self):

        return self._live_output.GetData()
    
#---------------------------------------------------------------------------

    def _ParseArguments(self, arguments):
        """
        @brief Parses the live output initialization data

        """
        
        if arguments.has_key('live_output'):

            configuration = arguments['live_output']


        else:

            raise Exception("No 'live_output' configuration block present")

        output_mode = None
        resolution = None
        
        if configuration.has_key('options'):

            options = configuration['options']

            if options.has_key('output_mode'):

                output_mode = options['output_mode']

            if options.has_key('resolution'):

                resolution = options['resolution']

            if options.has_key('append'):

                if options['append'] == '1':
                    
                    self.append = True

            if options.has_key('column_order'):

                if options['column_order'] == '1':

                    self.order = 'column'

        self._live_output = LiveOutput()

        self.SetMode(output_mode)

        self.SetResolution(resolution)


#---------------------------------------------------------------------------


    def _ParseOutputs(self):
        """!

        @brief Parses the set outputs from the schedule configuration.

        Outputs can also be set via a yaml string fed to the parse method.
        """

        if not self.outputs is None and not self.outputs_parsed:

            #
            # Could be possible to move this loop to it's own method
            # for loading outputs.
            #
            component_name = ""
            field = ""

            for i, o in enumerate(self.outputs):

                if o.has_key('outputclass'):

                    if o['outputclass'] != 'double_2_ascii':
                        # if this output is not meant
                        # for this object type then we
                        # continue and ignore it
                        continue

                if o.has_key('component_name'):
                    
                    component_name = o['component_name']

                else:

                    print "Output Error, no component name for output %d" % i

                    continue

                if o.has_key('field'):

                    field = o['field']

                else:

                    print "Output Error, no field given for output %d" % i

                    continue


                if self.verbose:

                    print "\tAdding output %d, '%s' with field '%s'" % (i+1, component_name, field)

                    
                self.AddAddressFromSolver(component_name, field)


            self.outputs_parsed = True
