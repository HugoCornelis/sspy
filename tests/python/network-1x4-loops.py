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
                                             type="model_container",
                                             verbose=True)

my_model_container.NDFLoadLibrary('cells/RScell-nolib.ndf', 'rscell')

my_model_container.SetParameter('::rscell::/cell/soma/Ex_channel', 'G_MAX', '0.04330736624')
my_model_container.SetParameter('::rscell::/cell/soma/Ex_channel', 'Erev', '0')

#
# Must create solver.
#
my_heccer = scheduler.CreateSolver('My solver', 'heccer', verbose=True)

# Sets the segment of the model to run from
my_heccer.SetModelName('/cell')

# set the timestep for the entire scheduler (solvers, inputs and outputs)
my_heccer.SetTimeStep(2e-05)


# Create a perfectclamp object for current holding.
my_input = scheduler.CreateInput('My perfectclamp','perfectclamp',verbose=True)




#
# Create Outputs
#
my_output = scheduler.CreateOutput('My output object', 'double_2_ascii')

my_output.SetFilename('/tmp/output')

my_output.AddOutput('/cell/soma', 'Vm')

# This should probably just be arg flags or something, passing 'steps'
# seems a bit tacky.
my_output.SetMode('steps')

my_output.SetResolution(10)



scheduler.Run(time=0.2)

print "Done!"
