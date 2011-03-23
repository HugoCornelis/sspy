#! /usr/bin/env python
"""

"""
import pdb
import os

from test_library import add_sspy_path

add_sspy_path()

from sspy import SSPy 


scheduler = SSPy()

try:
    
    scheduler.Load("./yaml/springmass3.yml")

except Exception, e:

    print e


scheduler.Run()

print "Done!"

