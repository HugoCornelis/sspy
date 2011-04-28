"""
This is the output plugin for outputting data
from connected solvers
"""
import os
import pdb
import sys

# this should go away later when I update the
# system path
#
sys.path.append("/usr/local/glue/swig/python")

try:

    import neurospaces.experiment.output as og

except ImportError, e:

    sys.exit("Error importing the Experiment Output Python module: %s\n" % e)


_default_filename = "/tmp/OutputGenerator"

class Output:

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
        
        self._output_gen = None

        self.output_mode = None

        self.filename = _default_filename
        
        self._outputs = None

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
        
        self._outputs = outputs
        
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

    def Initialize(self):

        pass
    
#---------------------------------------------------------------------------

    def Connect(self, solver):
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
        solver_type = solver.GetType()

        if solver_type == 'heccer':

            my_heccer = solver.GetCore()

            # Here we need to get the timestep and set it
            # for our object
            time_step = my_heccer.GetTimeStep()

            self.SetTimeStep(time_step)


            #
            # Could be possible to move this loop to it's own method
            # for loading outputs.
            #
            component_name = ""
            field = ""
            
            for i, o in enumerate(self._outputs):

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

                address = my_heccer.GetAddress(component_name, field)

                if self.verbose:

                    print "\tAdding output %d, '%s' with field '%s'" % (i+1,component_name, field)
                    
                self._output_gen.AddOutput(component_name, address)


#---------------------------------------------------------------------------


    def Step(self, time=None):
        """

        """
        self._output_gen.Step(time)


#---------------------------------------------------------------------------

    def Report(self):

        pass
    
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

                self.filename = None


        self._output_gen = og.Output(self.filename)

        
        if output_mode == 'steps':
            
            # turn on steps mode
            
            self._output_gen.SetSteps(1) 
            

        if resolution is not None:

            self._output_gen.SetResolution(resolution)


        if string_format is not None:

            self._output_gen.SetFormat(string_format)
