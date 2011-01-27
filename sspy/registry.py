"""!
@file registry.py

This module contains classes used to dynamically create
solvers and objects from plugin specifications. 
"""
import errors
import os
import pdb
import sys


#************************* Begin SolverRegistry ****************************
class SolverRegistry:
    """
    @class SolverRegistry 
    """


#---------------------------------------------------------------------------

    def __init__(self):

        curr_dir = os.path.dirname(os.path.abspath(__file__))

        self._solver_dir = os.path.join(curr_dir, "solvers")

        if not os.path.isdir(self._solver_dir):
        
            raise errors.SolverError("\"solvers\" directory not found")
        

#---------------------------------------------------------------------------

    def GetSolvers(self):

        """!
        @brief Returns the list of detected simulators.
        """

        solvers = self._FindSolvers()
    
        return solvers

#---------------------------------------------------------------------------

    def GetPlugins(self):

        """!
        @brief Returns the list of detected simulators.
        """
        pis = self._FindSolverPlugins()

        # exception?
    
        return pis

#---------------------------------------------------------------------------

    def _IsSolver(self, path):
        """

        """
        return os.path.isfile( os.path.join( path, 'solver.yml' ))

#---------------------------------------------------------------------------


    def _FindSolverPlugins(self):
        """!
        @brief Finds all solvers plugin files in the solvers_dir

        Returns a list of the plugin files. 
        """

        plugins = []

        for path, directories, files in os.walk( self._solver_dir ):
            if self._IsSolver( path ):
                path.replace( '/','.' )

                pi = path + "/solver.yml"
            
                plugins.append(pi)

        return plugins


#---------------------------------------------------------------------------

    def _FindSolvers(self):
        """!
        @brief Finds all solvers in the solvers_dir

        Returns a list of the solver directories 
        """

        solvers = []

        for path, directories, files in os.walk( self._solver_dir ):
            if self._IsSolver( path ):
                path.replace( '/','.' )
                
                solvers.append(path)

        return solvers

    
#---------------------------------------------------------------------------

#*************************** End SolverRegistry ****************************
