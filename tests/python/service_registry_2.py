#! /usr/bin/env python
"""
Test loads a user given service directory.
"""
import pdb
import os

from test_library import add_sspy_path

add_sspy_path()

from sspy.registry import ServiceRegistry

def print_service(s):

    print "Name is %s" % s.GetName()
    print "Module name is %s" % s.GetModuleName()
    print "Arguments are %s" % str(s.GetArguments())
    

sr = ServiceRegistry("tests/python/test_services/")


sps = sr.GetPlugins()

# for s in sps:

#     print "  Plugin name: %s" % s

my_service_1 = sr.CreateService("my service 1", "test")
my_service_2 = sr.CreateService("my service 2", "test 2")


print "Printing output of service 1"
print_service(my_service_1)

print "\n\nPrinting output of service 2"
print_service(my_service_2)


print "Done"
