#! /usr/bin/env python
"""
Test loads a user given solver directory.
"""
import pdb
import os

from test_library import add_sspy_path

add_sspy_path()

from sspy.registry1 import Registry

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

sr = Registry("tests/python/test_solvers/","solver.yml")


sps = sr.GetPlugins()

for s in sps:

    print "  Plugin name: %s" % s

print "Done"
