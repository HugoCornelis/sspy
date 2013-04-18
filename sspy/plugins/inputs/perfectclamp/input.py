"""
This is the input plugin for connecting an input
to a model.
"""
import os
import pdb
import sys

try:

    from experiment.perfectclamp import PerfectClamp

except ImportError, e:

    sys.exit("Error importing the experiment perfectclamp python module: %s\n" % e)


#---------------------------------------------------------------------------

class InputError(Exception):
    pass

#---------------------------------------------------------------------------

class Input:

    """!
    @brief class object for a perfectclamp input
    """
    
#---------------------------------------------------------------------------

    def __init__(self, name="Untitled PerfectClamp", plugin=None,
                 arguments=None, verbose=False):


        self._name = name

        self._plugin_data = plugin

        self.verbose = verbose

        self.time_step = 0.0
        
        self._perfectclamp = None

        # The only reason this is a list is because
        # we read in a list of data from the yaml specifications.
        # no real need for it since we can only set one input
        self.inputs = []

        self.inputs_parsed = False

        self.command_level = None

        self.command_file = None

        # This is the object to connect the input to solvers for addressing
        self._solver_collection = None

        self._perfectclamp = PerfectClamp(self._name)

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
    
    def AddInput(self, name, field, solver=None):
        """!

        Adds an input to the internal queue of inputs. Kind of silly
        since we can only really have one. To have several we'd need
        multiple objects.
        """

        input_entry = None

        if self._solver_collection is None:


            input_entry = dict(field=field, component_name=name, solver=solver, set=False)


        else:

            self.AddAddressFromSolver(name, field, solver=solver)

            input_entry = dict(field=field, component_name=name, solver=solver, set=True)


        self.inputs.append(input_entry)


#---------------------------------------------------------------------------

    def AddAddressFromSolver(self, name, field, solver=None):

        if self._solver_collection is None:

            raise Exception("Input Error: can't add output for %s, %s: No Solver" % (name, field))
            
        try:

            # Don't think we need to check for whether we have heccer or not.
            # depends on what solvers are deemed compatible. If so then we
            # retrieve the solver to determine the type first if solver is
            # not equal to None.

            address = self._solver_collection.GetAddress(name, field, solver)

            self._perfectclamp.AddInput(address)

        except Exception, e:

            raise Exception("Input Error: can't add input for %s %s: %s" % (name, field, e))
        
#---------------------------------------------------------------------------

    def SetInputs(self, inputs):
        """!
        @brief Sets the inputs for this object
        """
        self.inputs = inputs

#---------------------------------------------------------------------------

    def SetCommand(self, level):

        self._perfectclamp.SetCommand(level)

        self.command_level = level
        
#---------------------------------------------------------------------------

    def Advance(self):

        pass


#---------------------------------------------------------------------------

    def Connect(self, solvers):
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

        if solvers is None:

            raise Exception("Can't connect solvers to input '%s' of type '%s', no solvers exist" % (self.GetName(), self.GetType()))

        
        self._solver_collection = solvers

        time_step = self._solver_collection.GetTimeStep()

        self.SetTimeStep(time_step)

#        solver_type = solver.GetType()

        self.Initialize()

        component_name = ""
        field = ""
        solver = None

        for i, inp in enumerate(self.inputs):

            if inp.has_key('inputclass'):

                if inp['inputclass'] != 'perfectclamp':
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


            solver = inp['solver']

            address = self._solver_collection.GetAddress(component_name, field, solver)

            #exception?

            if self.verbose:

                print "\tConnecting input variable '%s -> '%s' from solvers" % (component_name, field)
                    
            self._perfectclamp.AddInput(address)

 
#---------------------------------------------------------------------------

    def _Connect(self, solver):
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

        self._solver_collection = solvers

        time_step = self._solver_collection.GetTimeStep()

        self.SetTimeStep(time_step)

        # if the internal object hasn't been created then we do it here
        self.Initialize()

        component_name = ""
        field = ""
        solver = None

        for i, inp in enumerate(self.inputs):

            if inp.has_key('inputclass'):

                if inp['inputclass'] != 'perfectclamp':
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


            # not much in the way of support for tagging a particular solver for an input here
            address = self._solver_collection.GetCompartmentAddress(component_name, field)

            #exception?

            if self.verbose:

                print "\tConnecting input variable '%s -> '%s' from solver '%s'" % (component_name, field, solver.GetName())
                    
            self._perfectclamp.AddInput(address)
                

#---------------------------------------------------------------------------

    def Finish(self):
        """

        """
        self._perfectclamp.Finish()

#---------------------------------------------------------------------------

    def Initialize(self):
        """!
        @brief Initializes the perfect clamp from any internal variables that were set
        """
        if self._perfectclamp is None:

            self._perfectclamp = PerfectClamp(self._name)

        if self._perfectclamp is None:

            raise Exception("Can't initialize the PerfectClamp object '%s'" % self._name)

        # Apply the parameters loaded or set via api

        if not self.command_level is None:

            if not self.command_file is None:

                self._perfectclamp.SetFields(self.command_level, self.command_file)
                
            else:
                
                self._perfectclamp.SetCommand(self.command_level)

#---------------------------------------------------------------------------

    def Reset(self):
        """!
        @brief Destroys and recreates the core perfectclamp object
        """

        
        self.Initialize()

#---------------------------------------------------------------------------

    def Compile(self):
        """
        @brief Compiles the perfectclamp input
        """
        self._perfectclamp.Compile()

#---------------------------------------------------------------------------

    def New(self):

        pass


#---------------------------------------------------------------------------

    def Step(self, time):
        """
        @brief performs a single step for the input
        """

        self._perfectclamp.Step(time)

#---------------------------------------------------------------------------

    def Report(self):

        pass

#---------------------------------------------------------------------------

    def _ParseArguments(self, arguments=None):
        """!
        @brief Parsed the input initialization data

        The block of yaml to parse looks like this:
            
          perfectclamp:
              module_name: Experiment
              options:
                  command: -0.06
                  name: purkinje cell perfect clamp
              package: Experiment::PerfectClamp

        Ignored Keys:

            ['perfectclamp']['package']
            ['perfectclamp']['module_name']
            
        """
        if arguments is None:

            return

        if arguments.has_key('perfectclamp'):

            configuration = arguments['perfectclamp']

        else:

            raise Exception("No 'perfectclamp' configuration block present")


        if configuration.has_key('options'):

            options = configuration['options']

            if options.has_key('command'):

                self.command_level = options['command']

            if options.has_key('name'):

                self._name = options['name']

            if options.has_key('filename'):

                self.command_file = options['filename']
            
#---------------------------------------------------------------------------


