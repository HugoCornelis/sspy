#! /usr/bin/env python
"""

"""
import pdb
import os

from test_library import add_sspy_path

add_sspy_path()

from sspy import SSPy 


scheduler = SSPy(verbose=True,
                 service_directory="tests/python/test_services/")

try:
    
    scheduler.Load("./tests/yaml/service_1.yml")

except Exception, e:

    print e


services = scheduler.GetLoadedServices()

for s in services:

    print "This service name is '%s'" % s.GetName()
