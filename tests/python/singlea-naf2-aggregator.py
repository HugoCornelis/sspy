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
    
    scheduler.Load("./tests/yaml/singlea-naf2-aggregator.yml")

except Exception, e:

    print e


scheduler.Run()
