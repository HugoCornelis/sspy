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

class Instance:

    """!
    @brief class object for a pulsegen input
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
        self.trigger_mode = 0

        self._solver = None

        self._pulsegen = PulseGen(self._name)

        self.disable = False

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

                my_heccer = solver.GetObject()
                
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

                my_heccer = solver.GetObject()
                
                address = my_heccer.GetCompartmentAddress(component_name, field)

                #exception?

                if self.verbose:

                    print "\tConnecting input variable '%s -> '%s' from solver '%s'" % (component_name, field, solver.GetName())
                    
                self._pulsegen.AddVariable(address)
                

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

            self._pulsegen = PulseGen(self._name,
                                      level1=float(self.level1),
                                      width1=float(self.width1),
                                      delay1=float(self.delay1),
                                      level2=float(self.level2),
                                      width2=float(self.width2),
                                      delay2=float(self.delay2),
                                      trigger_mode=int(self.trigger_mode)
                                      )

        else:

            self._pulsegen.SetFields(level1=float(self.level1),
                                     width1=float(self.width1),
                                     delay1=float(self.delay1),
                                     level2=float(self.level2),
                                     width2=float(self.width2),
                                     delay2=float(self.delay2),
                                     trigger_mode=int(self.trigger_mode)
                                     )


        if self._pulsegen is None:

            raise Exception("Can't initialize the PulseGen plugin object '%s'" % self._name)

#---------------------------------------------------------------------------

    def Reset(self):
        """!
        @brief resets the pulsegen back to it's precompiled state
        """

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

        if not self.disable:
            
            self._pulsegen.SingleStep(time)

#---------------------------------------------------------------------------

    def Report(self):
        pass


#---------------------------------------------------------------------------

    def SetLevel1(self,level1):

        self.level1 = level1

        if not self._pulsegen is None:
            
            self._pulsegen.SetLevel1(level1)

#---------------------------------------------------------------------------

    def GetLevel1(self):

        return self._pulsegen.GetLevel1()

#---------------------------------------------------------------------------

    def SetWidth1(self,width1):

        self.width1 = width1

        if not self._pulsegen is None:
            
            self._pulsegen.SetWidth1(width1)

#---------------------------------------------------------------------------

    def GetWidth1(self):

        return self._pulsegen.GetWidth1()

#---------------------------------------------------------------------------
    def SetDelay1(self,delay1):

        self.delay1 = delay1

        if not self._pulsegen is None:
            
            self._pulsegen.SetDelay1(delay1)

#---------------------------------------------------------------------------

    def GetDelay1(self):

        return self._pulsegen.GetDelay1()

#---------------------------------------------------------------------------

    def SetLevel2(self,level2):

        self.level2 = level2

        if not self._pulsegen is None:
            
            self._pulsegen.SetLevel2(level2)

#---------------------------------------------------------------------------

    def GetLevel2(self):

        return self._pulsegen.GetLevel2()

#---------------------------------------------------------------------------

    def SetWidth2(self,width2):

        self.width2 = width2

        if not self._pulsegen is None:
            
            self._pulsegen.SetWidth2(width2)

#---------------------------------------------------------------------------

    def GetWidth2(self):

        return self._pulsegen.GetWidth2()

#---------------------------------------------------------------------------

    def SetDelay2(self,delay2):

        self.delay2 = delay2

        if not self._pulsegen is None:
            
            self._pulsegen.SetDelay2(delay2)

#---------------------------------------------------------------------------

    def GetDelay2(self):

        return self._pulsegen.GetDelay2()

#---------------------------------------------------------------------------

    def SetBaseLevel(self,base_level):

        self.base_level = base_level

        if not self._pulsegen is None:
            
            self._pulsegen.SetBaseLevel(base_level)

#---------------------------------------------------------------------------

    def GetBaseLevel(self):

        return self._pulsegen.GetBaseLevel()

#---------------------------------------------------------------------------

    def SetTriggerMode(self,trigger_mode):

        self.trigger_mode = trigger_mode

        if not self._pulsegen is None:
            
            self._pulsegen.SetTriggerMode(trigger_mode)

#---------------------------------------------------------------------------

    def GetTriggerMode(self):

        return self._pulsegen.GetTriggerMode()

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


