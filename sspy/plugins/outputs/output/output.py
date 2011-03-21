"""
This is the output plugin for outputting data
from connected solvers
"""
import os
import pdb
import sys

# this should go away later when I update the
# 
sys.path.append("/usr/local/glue/swig/python")

try:

    import g3.experiment.output as og

except ImportError, e:

    sys.exit("Error importing the Experiment Output Python module: %s\n" % e)


#---------------------------------------------------------------------------


class Output:

#---------------------------------------------------------------------------

    def __init__(self,  name="Untitled solver", plugin=None, 
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

        self.filename = None
        
        self._outputs = None

        self._ParseArguments(arguments)


#---------------------------------------------------------------------------

    def Compile(self):
        """
        @brief 
        """
        self._output_gen.Compile()
        
#---------------------------------------------------------------------------

    def GetName(self):

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
        time_step = 0.01
        
        return time_step

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

        solver_type = solver.GetType()

        if solver_type == 'heccer':

            my_heccer = solver.GetCore()

            component_name = ""
            field = ""
            
            for i, o in enumerate(self._outputs):

                if o.has_key('outputclass'):

                    if o['outputclass'] != 'double_2_ascii':
                        # if this output is not meant
                        # for this object type then we
                        # continue
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
                #pdb.set_trace()
                address = my_heccer.GetAddress(component_name, field)

                if self.verbose:

                    print "\tAdding output '%s' with field '%s'" % (component_name, field)
                    
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


        if configuration.has_key('options'):

            options = configuration['options']

            if options.has_key('output_mode'):

                self.output_mode = options['output_mode']

            if options.has_key('filename'):

                self.filename = options['filename']

            else:

                self.filename = None

        self._output_gen = og.Output(self.filename)

            
        
        
