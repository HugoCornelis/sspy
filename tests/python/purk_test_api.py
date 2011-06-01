#! /usr/bin/env python
"""

"""
import pdb
import os
import sys

os.environ['NEUROSPACES_NMC_MODELS']='/usr/local/neurospaces/models/library'

from test_library import add_sspy_path

add_sspy_path()

from sspy import SSPy 


scheduler = SSPy(verbose=True)

my_model_container = None
#
# Create a model container service and load an ndf file
#
    
my_model_container = scheduler.CreateService(name="My Model Container",
                                             type="model_container")

my_model_container.Load('tests/cells/purk_test_segment.ndf')

#
# Create an perfectclamp input object
#
my_perfect_clamp = scheduler.CreateInput('Inject', 'perfectclamp')
pdb.set_trace()



scheduler.Run()
