#! /usr/bin/env python
"""

"""
import pdb
import os

from test_library import add_sspy_path

add_sspy_path()


from sspy import SSPy 


scheduler = SSPy(verbose=True)

print "printing the currently loaded services"

scheduler.ListServicePlugins()


try:

    print "Loading test service \'test\'"
    scheduler.LoadServicePlugin("./tests/python/test_services/test/service.yml")

    print "Loading test service \'test 2\'"
    scheduler.LoadServicePlugin("./tests/python/test_services/test_2/")

except Exception, e:

    print e


print "printing loaded service plugins after dynamically loading"

scheduler.ListServicePlugins()


