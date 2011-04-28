"""
A test library of functions and classes
for running heccer tests from python.

"""

import os
import sys
import pdb


def add_package_path(package):
    """
    Adds an import path to a python module in a project directory.
    """

    root_path = os.path.join(os.environ['HOME'],
                             'neurospaces_project',
                             package,
                             'source',
                             'snapshots',
                             '0')

    path = os.path.join(root_path, 'glue','swig', 'python')

    sys.path.append(path)



def add_sspy_path():
    """
    Adds an import path to a python module in a project directory.
    """
    
    sspy_path = os.path.join(os.environ['HOME'],
                             'neurospaces_project',
                             'sspy',
                             'source',
                             'snapshots',
                             '0')

    sys.path.append(sspy_path)


    

    
