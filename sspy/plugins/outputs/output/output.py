"""
This is the output plugin for outputting data
from connected solvers
"""
import os
import pdb
import sys

try:

    import experiment.output as og

except ImportError, e:

    sys.exit("Error importing the Experiment Output Python module: %s\n" % e)


_default_filename = "/tmp/OutputGenerator"

class Instance:

#---------------------------------------------------------------------------

    def __init__(self,  name="Untitled Output", plugin=None, filename=None,
                 arguments=None, verbose=False):

        self._name = name

        self._plugin_data = plugin

        self.verbose = verbose

        # should be inconsequential in an output object
        # it is only here for reporting purposes to keep
        # the object consistent when it's passed on to
        # the schedulee.
        self.time_step = 0.0
        
        self._output_gen = None

        self.filename = _default_filename

        self.format = None

        self.mode = None

        self.resolution = None
        
        self.outputs = []

        self.outputs_parsed = False

        self.append = False

        self.no_timestep = 0

        self.header = None

        self._solver_collection = None

        if not arguments is None:
            
            self._ParseArguments(arguments)

            

#---------------------------------------------------------------------------

    def Compile(self):
        """
        @brief 
        """
        self._output_gen.Compile()

#---------------------------------------------------------------------------

    def Finish(self):
        """
        @brief 
        """
        self._output_gen.Finish()

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

    def AddOutput(self, name, field, solver=None):
        """!

        @brief Adds an output to the solver


        Performs a check for the solver type. Any issues after the solver check
        should throw an exception. 
        """

        # The output entry gives all details for setting the output as well as a
        # status so we don't set the same one twice.
        output_entry = None

        if self._solver_collection is None:
            # if it's none then we store it for later use

            output_entry = dict(field=field,component_name=name,solver=solver,set=False)
            

        else:

            self.AddAddressFromSolver(name, field, solver)

            output_entry = dict(field=field,component_name=name,solver=solver,set=True)


        self.outputs.append(output_entry)
        
#---------------------------------------------------------------------------

    def AddAddressFromSolver(self, name, field, solver=None):
        """

        """
            
        if self._solver_collection is None:

            raise Exception("Output error: can't add output for %s, %s: No Solvers connected" % (name, field))
        
        try:

            address = self._solver_collection.GetAddress(name, field, solver)

            # here the name and address gets passed to the lower level object
            
            self._output_gen.AddOutput(name, address)
    
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

        self._output_gen.Finish()


#---------------------------------------------------------------------------

    def SetHeader(self, line):

        self.header = line

#---------------------------------------------------------------------------

    def WriteLine(self, line):

        if self._output_gen is None:

            raise Exception("Can't write line, output not initialized")
            
        elif line == "" or line == None:

            raise Exception("Can't write line, invalid or empty line")

        else:
            
            self._output_gen.WriteLine(line)


#---------------------------------------------------------------------------

    def Initialize(self):

        # if the output object is not built declaratively
        # then it must be built here just before connection to a solver. 
        if self._output_gen is None:

            self._output_gen = og.Output(self.filename)

            if self._output_gen is None:

                raise Exception("Can't create output generator object '%s'" % self.GetName())

            if not self.header is None:
            
                self._output_gen.WriteLine(self.header)

        # Here we set any output parameters we loaded into the plugin

        if not self.format is None:

            self._output_gen.SetFormat(self.format)


        if not self.mode is None:
            
            if self.mode == 'steps':
                        
                self._output_gen.SetSteps(1)


        if not self.resolution is None:

            self._output_gen.SetResolution(self.resolution)


        self._output_gen.NoTimeStep(self.no_timestep)

        
#---------------------------------------------------------------------------

    def Reset(self):
        """!
        @brief Destroys and recreates the core output object
        """

        if not self.append:

            self.Finish()

            self._output_gen = None
  
            if os.path.isfile(self.filename):
                
                os.remove(self.filename)

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
        self._output_gen.Step(time)


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

    def SetFormat(self, strfmt=None):
        """

        """

        self.format = strfmt

#---------------------------------------------------------------------------

    def SetAppend(self, append=False):

        self.append = append
    
#---------------------------------------------------------------------------

    def SetFilename(self, filename=None):
        """
        
        """
        if not filename:

            return
        
        self.filename = filename

#---------------------------------------------------------------------------

    def GetFilename(self):

        return self.filename

#---------------------------------------------------------------------------

    def NoTimeStep(self, v):

        self.no_timestep = v

        if not self._output_gen is None:
            
            self._output_gen.NoTimeStep(v)
        
#---------------------------------------------------------------------------

    def _ParseArguments(self, arguments):
        """
        @brief Parses the output initialization data

        Ignored keys:

            ['double_2_ascii']['options']['package']
            ['double_2_ascii']['module_name']
        """
        
        if arguments.has_key('double_2_ascii'):

            configuration = arguments['double_2_ascii']


        else:

            raise Exception("No 'double_2_ascii' configuration block present")

        output_mode = None
        resolution = None
        string_format = None
        append = False
        
        if configuration.has_key('options'):

            options = configuration['options']

            if options.has_key('output_mode'):

                output_mode = options['output_mode']

            if options.has_key('resolution'):

                resolution = options['resolution']

            if options.has_key('format'):

                string_format = options['format']

            if options.has_key('filename'):

                self.filename = options['filename']

            else:

                self.filename = _default_filename

            if options.has_key('append'):

                if options['append'] == '1':
                    
                    append = True

        self._output_gen = og.Output(self.filename)

        self.SetMode(output_mode)

        self.SetResolution(resolution)

        self.SetFormat(string_format)

        self.SetAppend(append)

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
            solver = None

            for i, o in enumerate(self.outputs):

                if o['set']:

                    # here if the output has been flagged as 'set' we skip it to prevent
                    # setting it again.
                    
                    continue
                    
                if o.has_key('outputclass'):

                    #! section is probably not needed anymore
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

                # This one is optional so we don't need to bail out or report if there's no entry
                if o.has_key('solver'):

                    solver = o['solver']


                if self.verbose:

                    print "\tAdding output %d, '%s' with field '%s'" % (i+1, component_name, field)

                    
                self.AddAddressFromSolver(component_name, field, solver)


            self.outputs_parsed = True
