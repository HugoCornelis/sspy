#! /usr/bin/env python
"""

"""
import pdb
import os

from test_library import add_sspy_path

add_sspy_path()

from sspy import SSPy 


scheduler = SSPy(verbose=True)

try:
    
    scheduler.Load("./tests/yaml/purk_test_soma.yml")

except Exception, e:

    print "Error while loading schedule file: %s" % e



scheduler.Run()


