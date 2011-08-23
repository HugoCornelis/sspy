"""!


"""
import os
import pdb
import sys

try:
    import yaml
except ImportError:
    sys.exit("Need PyYaml http://pyyaml.org/\n")


class SaveError(Exception):
    pass


indent = "  "

#*********************************** Begin Save ****************************

class Save:
    """
    Class exports the schledule to YAML. Has the potential to be pluggable
    with some simpl changes.
    """
    
#---------------------------------------------------------------------------
    
    def __init__(self, scheduler, filename=None):
        """
        @param scheduler Reference to the scheduler
        """
        
        self.scheduler = scheduler

        self.filename = None

#---------------------------------------------------------------------------

    def SetFilename(self, filename):

        self.filename = filename

#---------------------------------------------------------------------------

    def Analyzers(self):

        return dict(analyzers={})

#---------------------------------------------------------------------------

    def ApplicationClasses(self):

        pass

#---------------------------------------------------------------------------

    def Apply(self):
        """

        This apply block excludes the 'results' key.
        """

        steps = None
        time = None

        try:

            steps = self.scheduler.steps 

        except Exception:

            pass

        try:

            time = self.scheduler.simulation_time

        except Exception:

            pass

        simulations = []

        verbosity_level = self.scheduler.GetVerbosityLevel()

        if not steps is None:

            sim = dict(arguments=[steps, dict(verbose=verbosity_level)],
                       method='steps')

            simulations.append(sim)

        elif not time is None:

            sim = dict(arguments=[time, dict(verbose=verbosity_level)],
                       method='advance')

            simulations.append(sim)
            

        apply_block = dict(simulation=simulations)

        return yaml.dump(apply_block)

#---------------------------------------------------------------------------

    def Models(self):

        pass

    def Name(self):

        return dict(name=self.scheduler.GetName())

    def Optimize(self):

        pass

    def InputClasses(self):

        pass

    def Inputs(self):

        pass

    def OutputClasses(self):

        pass

    def Outputs(self):

        pass
    
    def Services(self):

        pass

    def SolverClasses(self):
        """
        Right now sspy (and ssp) only handles one solver per simulation.
        """
        solvers = self.scheduler.GetLoadedSolvers()

        if len(solvers) <= 0:

            return None

        else:

            if solvers[0].GetType() == 'heccer':

                pass

            elif solvers[0].GetType() == 'chemesis3':

                pass

#---------------------------------------------------------------------------







#************************************ End Save ****************************
