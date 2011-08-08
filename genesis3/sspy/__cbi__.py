"""
@file __cbi__.py

This file provides data for a packages integration
into the CBI architecture.
"""


__author__ = "Mando Rodriguez"
__copyright__ = "Copyright 2010, The GENESIS Project"
__credits__ = ["Mando Rodriguez","Hugo Cornelis","Allan Coop"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Mando Rodriguez"
__email__ = "mandorodriguez at gmail.com"
__requires__ = ['yaml']
__status__ = "Development"
__description__ = ("The simple scheduler in python is a software package that "
                   "uses the model container and heccer solver to run a simulation "
                   "with a set of simulation parameters. It can be extended by using "
                   "plugins for solvers and simulation objects.")
__url__ = "http://genesis-sim.org"
__download_url__ = "http://repo-genesis3.cbi.utsa.edu"

class PackageInfo:
    
    def GetRevisionInfo():
# $Format: "        return \"${monotone_id}\""$
        return "3d959be8f93bbe1a26a46c49c447ecaada263e80"

    def GetName():
# $Format: "        return \"${package}\""$
        return "sspy"

    def GetVersion():
# $Format: "        return \"${major}.${minor}.${micro}-${label}\""$
        return "0.0.0-alpha"

    def GetDependencies():
        """!
        @brief Provides a list of other CBI dependencies needed.
        """
        dependencies = []
        
        return dependencies
