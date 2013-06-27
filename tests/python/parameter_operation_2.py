#! /usr/bin/env python
"""

"""
import pdb
import os
import sys

os.environ['NEUROSPACES_NMC_MODELS']= os.path.join('/', 'usr', 'local', 'neurospaces', 'models', 'library')

from test_library import add_sspy_path

add_sspy_path()

from sspy import SSPy 


scheduler = SSPy(verbose=False)

my_model_container = None
#
# Create a model container service and load an ndf file
#
    
my_model_container = scheduler.CreateService(name="My Model Container",
                                             type="model_container")

my_model_container.Load('tests/cells/purk_test.ndf')

my_model_container.SetParameter('/purk_test/segments/soma',
                                'INJECT',
                                2e-09)


element = '/purk_test/segments/soma'

print ""
print "Parameters on '%s' before compile" % element

params = scheduler.GetAllParameters(element)

for k in params.iterkeys():

    print "%s: %s" % (k, params[k])

print ""

#
# Must create solver.
#
my_heccer = scheduler.CreateSolver('My solver', 'heccer')

# Sets the segment of the model to run from
my_heccer.SetModelName('/purk_test')

# set the timestep for the entire scheduler (solvers, inputs and outputs)
my_heccer.SetTimeStep(2e-05)

scheduler.RunPrepare()

print "Parameters on '%s' after compile" % element

params = scheduler.GetAllParameters('/purk_test/segments/soma')

for k in params.iterkeys():

    print "%s: %s" % (k, params[k])

print ""

print "Done!"
