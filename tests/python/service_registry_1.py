#! /usr/bin/env python
"""

"""
import pdb
import os

from test_library import add_sspy_path

add_sspy_path()

from sspy.registry import ServiceRegistry

sr = ServiceRegistry("tests/python/test_services/")

print "List of plugins:"
print sr.GetPluginFiles()

print "\nList of loaded service plugins:"

sps = sr.GetPlugins()

sps.sort()

for s in sps:

    print "  Plugin name: %s" % s

print "Done"
