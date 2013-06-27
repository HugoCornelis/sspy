#! /usr/bin/env python
"""

"""
import pdb
import os

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

my_model_container.Load('tests/cells/singlep.ndf')




#
# Must create solver.
#
my_heccer = scheduler.CreateSolver('My solver', 'heccer')

# Sets the segment of the model to run from
my_heccer.SetModelName('/singlep')

# set the timestep for the entire scheduler (solvers, inputs and outputs)
my_heccer.SetTimeStep(1e-05)



#
# Create a perfectclamp object for current holding.
#
my_input = scheduler.CreateInput('purkinje cell perfect clamp','perfectclamp')

my_input.AddInput('/singlep/segments/soma', 'Vm')

my_input.SetCommand(-0.06)



my_output = scheduler.CreateOutput('My output object', 'double_2_ascii')

my_output.SetFilename('/tmp/output')

my_output.AddOutput('/singlep/segments/soma', 'Vm')

# This is the default
my_output.SetAppend(False)

scheduler.Run(steps=10)

scheduler.Reset()

scheduler.Run(steps=10, finish=True)

print "Done!"

