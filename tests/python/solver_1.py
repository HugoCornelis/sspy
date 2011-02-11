#! /usr/bin/env python
"""

"""
import pdb
import os

from test_library import add_sspy_path

add_sspy_path()

from sspy import SSPy 


scheduler = SSPy(verbose=True,
                 solver_directory="tests/python/test_solvers/",
                 service_directory="tests/python/test_services/")

try:
    
    scheduler.Load("./tests/yaml/solver_1.yml")

except Exception, e:

    print e


scheduler.Dump()
