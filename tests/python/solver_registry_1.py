#! /usr/bin/env python
"""

"""
import pdb
import os

from test_library import add_sspy_path

add_sspy_path()

from sspy.registry import SolverRegistry

sr = SolverRegistry("tests/python/test_solvers/","solver.yml")

print "List of plugins:"
print sr.GetPluginFiles()

print "\nList of loaded solver plugins:"

sps = sr.GetPlugins()

for s in sps:

    print "  Plugin name: %s" % s

print "Done"
