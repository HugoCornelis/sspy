"""
@package _solver_collection

This module contains the SolverCollection class. This class
contains an object that keeps track of all solvers in the schedule
and all solver registries.


"""

import errors


class SolverCollection:

#---------------------------------------------------------------------------

    def __init__(self):

        self.solvers = []

#---------------------------------------------------------------------------

    def AddSolver(self, solver):

        for s in self._solvers:

            if solver.GetName() == s.GetName():

                # This exception should never be triggered since we check this
                # in the solver registry but it's here just in case.
                raise Exception("Solver collection error: Already a solver with the name '%s'" % s.GetName())

            
        self.solvers.append(solver)
            
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

    def GetAddress(self, path, field, solver_name=None):

        address = None
        solver = None
        
        if len(self.solvers) == 1:

            solver = self.solvers[0]

            address = solver.GetAddress(path, field)


        if not solver_name is None:

            # is we get a solver name then we just grab it

            solver = self.GetSolver(name)

            address = solver.GetAddress(path, field)

        else:

            # here we check each solver for the address
            # this is probably stupid. But we only do it when
            # we have multiple solvers so we'll deal with it.

            for s in self.solvers:

                address = s.GetAddress(path, field)

                if not address is None:
                    
                    # if we've found the address
                    # we break if not, it will end
                    # up as none anyway.
                    break


        return address
