"""
This is the input plugin for connecting an input
to a model.
"""
import os
import pdb
import sys

try:

    from experiment.pulsegen import PulseGen

except ImportError, e:

    sys.exit("Error importing the experiment pulsegen python module: %s\n" % e)


#---------------------------------------------------------------------------

class InputError(Exception):
    pass

#---------------------------------------------------------------------------

class Input:

    """!
    @brief class object for a perfectclamp input
    """
    
#---------------------------------------------------------------------------

    def __init__(self, name="Untitled Pulsegen", plugin=None,
                 arguments=None, verbose=False):


        self._name = name

        self._plugin_data = plugin

        self.verbose = verbose

        self.time_step = 0.0
        
        self._pulsegen = None
        
        self._inputs = []

        self.level1 = None
        self.level2 = None
        self.delay1 = None
        self.delay2 = None
        self.width1 = None
        self.width2 = None
        self.base_level = None
        self.trigger_mode = None

        self._solver = None

        self._pulsegen = PerfectClamp(self._name)

        self._ParseArguments(arguments)


#---------------------------------------------------------------------------

    def Format(self):
        
        """
        @brief Prints the text block format that is parsed for the input
        """
        return self._plugin_data.GetFormat()
            
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
    
    def AddInput(self, name, field):

        if self._solver is None:

            self._inputs.append(dict(field=field,component_name=name))

#            raise Exception("Can't add input to %s, it is not connected to a solver" % self.GetName())

        else:

            solver_type = self._solver.GetType()

            if solver_type == "heccer":

                my_heccer = solver.GetCore()
                
                address = my_heccer.GetCompartmentAddress(component_name, field)

                self._pulsegen.AddInput(address)

#---------------------------------------------------------------------------

    def SetInputs(self, inputs):
        """!
        @brief Sets the inputs for this object
        """
        self._inputs = inputs

#---------------------------------------------------------------------------

    def SetCommandVoltage(self, voltage):

        self._pulsegen.SetCommandVoltage(voltage)

        self.command_voltage = voltage
        
#---------------------------------------------------------------------------

    def Advance(self):

        pass


#---------------------------------------------------------------------------

    def Connect(self, solver):
        """!
        @brief Connects the input to a solvers input variable

        To properly connect an input to a solver you must:


            1. Retrieve the timestep from the solver and set it
            with the SetTimeStep method to ensure the scheudlee
            properly updates the object.

            2. Connect the solver core to the input core.

            3. Add the inputs via whatever method the cores use
            to communicate.
        
        """

        time_step = solver.GetTimeStep()

        self.SetTimeStep(time_step)

        solver_type = solver.GetType()

        self.Initialize()

        component_name = ""
        field = ""

        for i, inp in enumerate(self._inputs):

            if inp.has_key('inputclass'):

                if inp['inputclass'] != 'pulsegen':
                    # if this output is not meant
                    # for this object type then we
                    # continue and ignore it
                    continue

            if inp.has_key('component_name'):

                component_name = inp['component_name']

            else:

                print "Input Error, no component name for input %d" % i

                continue

            if inp.has_key('field'):

                field = inp['field']

            else:

                print "Input Error, no field given for input %d" % i

            if solver_type == 'heccer':

                my_heccer = solver.GetCore()
                
                address = my_heccer.GetCompartmentAddress(component_name, field)

                #exception?

                if self.verbose:

                    print "\tConnecting input variable '%s -> '%s' from solver '%s'" % (component_name, field, solver.GetName())
                    
                self._pulsegen.AddInput(address)
                

#---------------------------------------------------------------------------

    def Finish(self):
        """

        """
        self._pulsegen.Finish()

#---------------------------------------------------------------------------

    def Initialize(self):
        """!
        @brief Initializes the pulsegen from any internal variables that were set
        """
        if self._pulsegen is None:

            self._pulsegen = PerfectClamp(self._name,
                                          level1=self.level1, width1=self.width1, delay1=self.delay1,
                                          level2=self.level2, width2=self.width2, delay2=self.delay2,
                                          trigger_mode=self.trigger_mode
                                          )

        else:

            self._pulsegen.SetFields(level1=self.level1, width1=self.width1, delay1=self.delay1,
                                     level2=self.level2, width2=self.width2, delay2=self.delay2,
                                     trigger_mode=self.trigger_mode
                                     )

        if self._pulsegen is None:

            raise Exception("Can't initialize the PulseGen plugin object '%s'" % self._name)


#---------------------------------------------------------------------------

    def Reset(self):
        """!
        @brief Destroys and recreates the core perfectclamp object
        """

        
        self._pulsegen = None

        self.Initialize()

#---------------------------------------------------------------------------

    def Compile(self):
        """
        @brief Compiles the pulsegen input
        """
        self._pulsegen.Compile()

#---------------------------------------------------------------------------

    def New(self):

        pass


#---------------------------------------------------------------------------

    def Step(self, time):
        """
        @brief performs a single step for the input
        """
        self._pulsegen.Step(time)

#---------------------------------------------------------------------------

    def Report(self):

        pass

#---------------------------------------------------------------------------

    def _ParseArguments(self, arguments=None):
        """!
        @brief Parsed the input initialization data

        The block of yaml to parse looks like this:
            
            inputclasses:
                pulsegen:
                    module_name: Experiment
                    options:
                        level1: 50.0
                        width1: 3.0
                        delay1: 5.0
                        level2: -20.0
                        width2: 5.0
                        delay2: 8.0
                        baselevel: 10.0
                        triggermode: 0
                        
        Ignored Keys:

            ['pulsegen']['package']
            ['pulsegen']['module_name']
            
        """
        if arguments is None:

            return

        if arguments.has_key('pulsegen'):

            configuration = arguments['pulsegen']

        else:

            raise Exception("No 'pulsegen' configuration block present")


        if configuration.has_key('options'):

            options = configuration['options']

            if options.has_key('level1'):

                self.level1 = options['level1']

            if options.has_key('width1'):

                self.width1 = options['width1']

            if options.has_key('delay1'):

                self.delay1 = options['delay1']

            if options.has_key('level2'):

                self.level2 = options['level2']

            if options.has_key('width2'):

                self.width2 = options['width2']

            if options.has_key('delay2'):

                self.delay2 = options['delay2']

            if options.has_key('triggermode'):

                self.trigger_mode = options['triggermode']

#---------------------------------------------------------------------------


