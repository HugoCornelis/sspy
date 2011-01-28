#! /usr/bin/env python
"""
Test loads a user given solver directory.
"""
import pdb
import os

from test_library import add_sspy_path

add_sspy_path()

from sspy.registry import SolverRegistry

def print_solver(s):

    s.New()
    s.Advance()
    s.Compile()
    s.Connect()
    s.Deserialize()
    s.DeserializeState()
    s.Finish()
    s.Name()
    s.SetSolverField()
    s.GetSolverField()
    s.Serialize()
    s.SerializeState()
    s.Output()
    s.Run()
    s.Step()
    s.Steps()

sr = SolverRegistry("tests/python/test_solvers/")


sps = sr.GetPlugins()

for s in sps:

    print "  Plugin name: %s" % s

my_solver_1 = sr.CreateSolver("my solver 1", "test")
my_solver_2 = sr.CreateSolver("my solver 2", "test 2")


print "Printing output of solver 1"
print_solver(my_solver_1)

print "\n\nPrinting output of solver 2"
print_solver(my_solver_2)


print "Done"
