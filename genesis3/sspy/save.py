"""!


"""
import os
import pdb
import sys

try:
    import yaml
except ImportError:
    sys.exit("Need PyYaml http://pyyaml.org/\n")


#*********************************** Begin Save ****************************

class Save:
    """
    Class exports the schledule to YAML.
    """

    def __init__(self, scheduler):
        """
        @param scheduler Reference to the scheduler
        """
        
        self.scheduler = scheduler


#---------------------------------------------------------------------------





#************************************ End Save ****************************
