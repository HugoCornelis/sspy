#! /usr/bin/env python
"""

"""
import pdb
import os

os.environ['NEUROSPACES_NMC_MODELS']= os.path.join('/', 'usr', 'local', 'neurospaces', 'models', 'library')

from test_library import add_sspy_path

add_sspy_path()

from sspy import SSPy 


scheduler = SSPy(verbose=False)

try:
    
    scheduler.Load("./yaml/purk_test.yml")

except Exception, e:

    print "Error while loading schedule file: %s" % e


elements = scheduler.GetElements()

print "Top level child is: %s" % elements[0]
print "Number of elements is %s" % len(elements)



coords = scheduler.GetCoordinates()

print "Number of coordinates is %s" % len(coords)

print "Done!"


