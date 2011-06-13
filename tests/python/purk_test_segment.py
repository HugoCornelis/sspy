#! /usr/bin/env python
"""

"""
import pdb
import os

os.environ['NEUROSPACES_NMC_MODELS']='/usr/local/neurospaces/models/library'

from test_library import add_sspy_path

add_sspy_path()

from sspy import SSPy 


scheduler = SSPy(verbose=True)

try:
    
    scheduler.Load("./yaml/purk_test_segment.yml")

except Exception, e:

    print "Error while loading schedule file: %s" % e


scheduler.Run()

print "Done!"
