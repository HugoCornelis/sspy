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


scheduler = SSPy(verbose=True)

my_model_container = None
#
# Create a model container service and load an ndf file
#
    
my_model_container = scheduler.CreateService(name="My Model Container",
                                             type="model_container")

my_model_container.Load('tests/cells/purk_test_soma.ndf')

my_model_container.SetParameter('/purk_test_soma/segments/soma',
                                'INJECT',
                                2e-09)

#
# Must create solver.
#
my_heccer = scheduler.CreateSolver('My solver', 'heccer')

# Sets the segment of the model to run from
my_heccer.SetModelName('/purk_test_soma')

# set the timestep for the entire scheduler (solvers, inputs and outputs)
my_heccer.SetTimeStep(1e-06)


#
# Create Outputs
#
my_output = scheduler.CreateOutput('My output object', 'double_2_ascii')

my_output.SetFilename('/tmp/purk_test_soma_aggregators')

my_output.AddOutput('/purk_test_soma/segments/soma', 'Vm')

scheduler.Run(steps=5000, finish=True)

print "Done!"
