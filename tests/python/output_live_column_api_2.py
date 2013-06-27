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


my_output = scheduler.CreateOutput('output_object', 'live_output')

my_output.AddOutput('/singlep/segments/soma', 'Vm')

my_output.SetAppend(False)

my_output.SetOrder('column')

scheduler.Run(steps=5)

output1 = my_output.GetData()


for i in range(0,len(output1[0])):

    print "Timestep: %f, Vm: %f" % (output1[0][i], output1[1][i])



scheduler.Reset()

scheduler.Run(steps=5, finish=True)

output2 = my_output.GetData()


for i in range(0,len(output2[0])):

    print "Timestep: %f, Vm: %f" % (output2[0][i], output2[1][i])


print "Done!"

