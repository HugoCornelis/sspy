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
    
    scheduler.Load("./yaml/pulsegen_freerun.yml")

except Exception, e:

    print "Error while loading schedule file: %s" % e



scheduler.Run(finish=True)


