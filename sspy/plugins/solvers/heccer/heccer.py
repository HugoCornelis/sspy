"""
This is the solver plugin for Heccer to interact with
the interface of SSPy.
"""
import os
import pdb
import sys

# this should go away later when I update the
# 
sys.path.append("/usr/local/glue/swig/python")

try:
    
    import g3.heccer as heccer
    from g3.heccer import Heccer
    from g3.heccer import HeccerOptions

except ImportError, e:

    sys.exit("Error importing the Heccer Python module: %s\n" % e)


class Solver:

#---------------------------------------------------------------------------

    def __init__(self,  name="Untitled solver", plugin=None, 
                 constructor_settings=None, verbose=False):
        """

        Should be able to pass the scheudler and use it as
        an internal member here.
        """
        self._name = name

        self._plugin_data = plugin

        self.verbose = verbose
        
        self._heccer = None

        self.dump_options = (heccer.heccer_base.HECCER_DUMP_INDEXERS_SUMMARY
		   | heccer.heccer_base.HECCER_DUMP_INDEXERS_STRUCTURE
		   | heccer.heccer_base.HECCER_DUMP_INTERMEDIARY_COMPARTMENTS_PARAMETERS
		   | heccer.heccer_base.HECCER_DUMP_INTERMEDIARY_COMPARTMENT_SUMMARY
		   | heccer.heccer_base.HECCER_DUMP_INTERMEDIARY_MECHANISM_SUMMARY
		   | heccer.heccer_base.HECCER_DUMP_INTERMEDIARY_STRUCTURE
		   | heccer.heccer_base.HECCER_DUMP_INTERMEDIARY_SUMMARY
		   | heccer.heccer_base.HECCER_DUMP_TABLE_GATE_SUMMARY
		   | heccer.heccer_base.HECCER_DUMP_TABLE_GATE_TABLES
		   | heccer.heccer_base.HECCER_DUMP_VM_COMPARTMENT_MATRIX
		   | heccer.heccer_base.HECCER_DUMP_VM_COMPARTMENT_MATRIX_DIAGONALS
		   | heccer.heccer_base.HECCER_DUMP_VM_COMPARTMENT_OPERATIONS
		   | heccer.heccer_base.HECCER_DUMP_VM_MECHANISM_DATA
		   | heccer.heccer_base.HECCER_DUMP_VM_MECHANISM_OPERATIONS
		   | heccer.heccer_base.HECCER_DUMP_VM_CHANNEL_POOL_FLUXES
		   | heccer.heccer_base.HECCER_DUMP_VM_SUMMARY
		   | heccer.heccer_base.HECCER_DUMP_VM_AGGREGATORS)

#         if self._heccer is None:

#             raise Exception("Can't create Heccer solver '%s'" % name)

        time_step = -1
        
        if constructor_settings.has_key('service_name'):

            self._service_name = constructor_settings['service_name']

        # This will probably be unneeded in python
        if constructor_settings.has_key('module_name'):

            self._module_name = constructor_settings['module_name']

        if constructor_settings.has_key('configuration'):

            self._configuration = constructor_settings['configuration']

            # set configuration
        
        if constructor_settings.has_key('dStep'):

            time_step = constructor_settings['dStep']


        elif constructor_settings.has_key('step'):

            time_step = constructor_settings['step']
            

        if time_step > -1:
        
            self._heccer.SetTimeStep(time_step)
            

        self._compiled = False



        #self._heccer.SetTimeStep(time_step)

#---------------------------------------------------------------------------
        
    def Initialize(self):

        self._heccer.Initiate()

#---------------------------------------------------------------------------

    def GetName(self):

        return self._name


#---------------------------------------------------------------------------

    def GetType(self):

        return self._plugin_data.GetName()


#---------------------------------------------------------------------------

    def SetConfiguration(self, config):

        pass

#---------------------------------------------------------------------------

    def New(self, modelname, filename):

        print "Modelname %s, Filename %s" % (modelname, filename)
        

#---------------------------------------------------------------------------

    def Advance(self):

        pass

#---------------------------------------------------------------------------

    def Compile(self):
        """
        @brief 
        """
        if self._compiled is False:

            self._heccer.CompileAll()

            self._compiled = True

#---------------------------------------------------------------------------

    def IsCompiled(self):

        return self._compiled

#---------------------------------------------------------------------------

    def Connect(self, service=None):
        """!
        @brief Connects a service to the this solver

        Compatible services need to be coded into this method.

        Much like the ns-sli, the heccer object can only really
        be created when we know which service it will be connected
        to.
        """

        if not service:

            raise Exception("No service to connect to solver '%s'" % self.GetName())


        service_type = service.GetType()


        if service_type == "heccer_intermediary":

            intermediary = service.GetCore()

            if not intermediary:

                raise Exception("Heccer Intermediary is not defined")

            else:


                self._heccer = Heccer(name=self._name, pinter=intermediary)

                self._heccer.CompileAll()

        elif service_type == "model_container":

            model_container = service.GetCore()

            if not model_container:

                raise Exception("Model Container is not defined")

            else:

                self._heccer = Heccer(name=self._name, model=model_container)


        else:

            raise Exception("Incompatible Service")

#---------------------------------------------------------------------------

    def Deserialize(self, filename):

        pass

#---------------------------------------------------------------------------

    def DeserializeState(self, filename):

        pass

#---------------------------------------------------------------------------

    def Finish(self):

        pass

#---------------------------------------------------------------------------

    def Name(self):

        return self._name

#---------------------------------------------------------------------------

    def SetSolverField(self, field, value):

        pass

#---------------------------------------------------------------------------

    def GetSolverField(self, field):

        pass

#---------------------------------------------------------------------------


    def Serialize(self, filename):

        pass

#---------------------------------------------------------------------------

    def SerializeState(self, filename):

        pass

#---------------------------------------------------------------------------
        
    def Output(self, serial, field):

        print "Serial and field is %s:%s" % (serial, field)

#---------------------------------------------------------------------------

    def Run(self, time):

        print "Simulation time is %s" % time

#---------------------------------------------------------------------------

    def Step(self, time=None):
        """

        """
        if self._heccer is not None:

            self._heccer.Step(time)

            if self.verbose:

                self._heccer.Dump(0, self.dump_options)

        else:

            raise Exception("No simulation time given")

#---------------------------------------------------------------------------

    def Steps(self, steps):

        pass

  
