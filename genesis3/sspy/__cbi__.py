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

def GetRevisionInfo(self):
# $Format: "    return \"${monotone_id}\""$
    return "b676f85605976d49c51e5db6e82c20ebc0b2a8c7"

def GetPackageName(self):
# $Format: "    return \"${package}\""$
    return "sspy"

def GetVersion(self):
# $Format: "    return \"${major}.${minor}.${micro}-${label}\""$
    return "0.0.0-alpha"

def GetDependencies(self):
    """!
    @brief Provides a list of other CBI dependencies needed.
    """
    dependencies = []

    return dependencies

