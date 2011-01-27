#! /usr/bin/env python
"""

"""
import pdb
import os

from test_library import add_sspy_path

add_sspy_path()

from sspy.registry import SolverRegistry

sr = SolverRegistry()

print "List of plugins"
print sr.GetPlugins()

print "\nList of solver directories"
print sr.GetSolvers()

print "Done"
