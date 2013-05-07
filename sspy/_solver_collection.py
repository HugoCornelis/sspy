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

    def GetSolver(self, name):

        for s in self.solvers:

            if name == s.GetName():

                return s

        return None

#---------------------------------------------------------------------------

    def GetTimeStep(self):
        """

        Returns the used timestep.  If there are several solvers
        present then the smallest time step will be used.
        """
        
        result = self.time_step
        
        if self.time_step is None:

            for s in self.solvers:

                ts = s.GetTimeStep()

                if result is None:

                    result = ts

                if not ts is None and ts < result:

                    result = ts

#                 print "*** time step %s: %s -> %s " % (result, s.GetName(), ts)

            self.time_step = result

        return result

#---------------------------------------------------------------------------

    def GetAddress(self, path, field, solver_name=None):
        """

        Retrieves the address for a particular solver in the
        solver collection.
        """
        
        address = None
        solver = None

        error = None
            
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


                try:

                    address = s.GetObject().GetAddress(path, field)

                except Exception, e:

                    error = e

                if not address is None:
                    
                    # if we've found the address
                    # we break if not, it will end
                    # up as none anyway.
                    break

        if not address is None:
            
            return address

        else:

            if error is None:

                error = "Cannot find the address of %s -> %s" % (path, field)

            raise Exception(error)

           

#---------------------------------------------------------------------------

    def GetCompartmentAddress(self, path, field, solver_name=None):
        """

        Retrieves the address for a particular solver in the
        solver collection.
        """
        
        address = None
        solver = None
            
        if len(self.solvers) == 1:
            
            # If there's only one solver then we just address the one

            solver = self.solvers[0]

            address = solver.GetObject().GetCompartmentAddress(path, field)


        if not solver_name is None:

            # is we get a solver name then we just grab it

            solver = self.GetSolver(solver_name)

            address = solver.GetObject().GetCompartmentAddress(path, field)

        else:

            # here we check each solver for the address
            # this is probably stupid. But we only do it when
            # we have multiple solvers so we'll deal with it.

            for s in self.solvers:

                address = s.GetObject().GetCompartmentAddress(path, field)

                if not address is None:
                    
                    # if we've found the address
                    # we break if not, it will end
                    # up as none anyway.
                    break


        return address
