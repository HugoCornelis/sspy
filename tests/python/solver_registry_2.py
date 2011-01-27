#! /usr/bin/env python
"""

"""
import pdb
import os

from test_library import add_sspy_path

add_sspy_path()

from sspy.registry import SolverRegistry

sr = SolverRegistry()

my_solver = sr.CreateSolver("my solver", "heccer")

pdb.set_trace()

print "Done"
