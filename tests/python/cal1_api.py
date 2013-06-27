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

my_model_container.Load('chemesis/cal1.ndf')

#
# Must create solver.
#
my_chemesis3 = scheduler.CreateSolver('My Chemesis3', 'chemesis3')

# Sets the segment of the model to run from
my_chemesis3.SetModelName('/cal1')

# set the timestep for the entire scheduler (solvers, inputs and outputs)
my_chemesis3.SetTimeStep(0.002)


#
# Create Outputs
#
my_output = scheduler.CreateOutput('My output object', 'double_2_ascii')

my_output.SetFilename('/tmp/output_cal1_ssp')

my_output.AddOutput('/cal1/somaCa', 'concentration')
my_output.AddOutput('/cal1/somaCabuf', 'concentration')
my_output.AddOutput('/cal1/somabuf', 'concentration')

scheduler.Run(steps=1000)

print "Done!"
