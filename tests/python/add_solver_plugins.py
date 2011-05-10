#! /usr/bin/env python
"""

"""
import pdb
import os

from test_library import add_sspy_path

add_sspy_path()


from sspy import SSPy 


scheduler = SSPy(verbose=True)

print "printing the currently loaded solvers"

scheduler.ListSolverPlugins()


try:

    print "Loading test solver \'test\'"
    scheduler.LoadSolverPlugin("./tests/python/test_solvers/test/solver.yml")

    print "Loading test solver \'test 2\'"
    scheduler.LoadSolverPlugin("./tests/python/test_solvers/test_2/")

except Exception, e:

    print e


print "printing loaded solver plugins after dynamically loading"

scheduler.ListSolverPlugins()


