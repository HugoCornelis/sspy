"""
@package _solver_collection

This module contains the SolverCollection class. This class
contains an object that keeps track of all solvers in the schedule
and all solver registries. It takes the place of a basic solver list
that was used previously, so now we can pass this solver collection to
all outputs and allow them to address all solvers for output variables.


"""

import errors


class SolverCollection:

#---------------------------------------------------------------------------

    def __init__(self):


        self.time_step = None

        self.solvers = []

#---------------------------------------------------------------------------

    def AddSolver(self, solver):

        for s in self.solvers:

            if solver.GetName() == s.GetName():

                # This exception should never be triggered since we check this
                # in the solver registry but it's here just in case.
                raise Exception("Solver collection error: Already a solver with the name '%s'" % s.GetName())

            
        self.solvers.append(solver)

#---------------------------------------------------------------------------

    def GetNames(self):

        pass

#---------------------------------------------------------------------------

    def GetSolver(self, name):

        for s in self.solvers:

            if name == s.GetName():

                return s

        return None

#---------------------------------------------------------------------------

    def GetSolvers(self):

        return self.solvers

#---------------------------------------------------------------------------

    def SetTimeStep(self, time_step):

        self.time_step = time_step

        for s in self.solvers:

            s.SetTimeStep(time_step)
            
#---------------------------------------------------------------------------

    def GetTimeStep(self):
        """

        Returns the given timestep. If there are several solvers present
        then the time step will be set to the first value given.
        """
        
        ts = None
        
        if self.time_step is None:

            for s in self.solvers:

                ts = s.GetTimeStep()

                if not ts is None:

                    self.time_step = ts

                    break

        return self.time_step

#---------------------------------------------------------------------------

    def GetAddress(self, path, field, solver_name=None):
        """

        Retrieves the address for a particular solver in the
        solver collection.
        """
        
        address = None
        solver = None
            
        if len(self.solvers) == 1:
            
            # If there's only one solver then we just address the one

            solver = self.solvers[0]

            address = solver.GetObject().GetAddress(path, field)


        if not solver_name is None:

            # is we get a solver name then we just grab it

            solver = self.GetSolver(solver_name)

            address = solver.GetObject().GetAddress(path, field)

        else:

            # here we check each solver for the address
            # this is probably stupid. But we only do it when
            # we have multiple solvers so we'll deal with it.

            for s in self.solvers:

                address = s.GetObject().GetAddress(path, field)

                if not address is None:
                    
                    # if we've found the address
                    # we break if not, it will end
                    # up as none anyway.
                    break


        return address
