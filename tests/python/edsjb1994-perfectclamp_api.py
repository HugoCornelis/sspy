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

my_model_container.Load('cells/purkinje/edsjb1994.ndf')


#
# Must create solver.
#
my_heccer = scheduler.CreateSolver('My solver', 'heccer')

# Not sure wether to give this a get/set method 
my_heccer.options = 4

my_heccer.SetGranularity(1000)

# Sets the segment of the model to run from
my_heccer.SetModelName('/Purkinje')

# set the timestep for the entire scheduler (solvers, inputs and outputs)
my_heccer.SetTimeStep(2e-05)


#
# Create a perfectclamp object for current holding.
#
my_input = scheduler.CreateInput('purkinje cell perfect clamp','perfectclamp')

my_input.AddInput('/Purkinje/segments/soma', 'Vm')

my_input.SetCommand(-0.06)


#
# Create Outputs
#
my_output = scheduler.CreateOutput('My output object', 'double_2_ascii')

my_output.SetFilename('/tmp/output')

my_output.AddOutput('/Purkinje/segments/soma', 'Vm')
my_output.AddOutput('/Purkinje/segments/b0s01[0]', 'Vm')
my_output.AddOutput('/Purkinje/segments/b0s03[56]', 'Vm')
my_output.AddOutput('/Purkinje/segments/b1s06[137]', 'Vm')
my_output.AddOutput('/Purkinje/segments/b1s12[26]', 'Vm')
my_output.AddOutput('/Purkinje/segments/b2s30[3]', 'Vm')
my_output.AddOutput('/Purkinje/segments/b3s44[49]', 'Vm')

# This should probably just be arg flags or something, passing 'steps'
# seems a bit tacky.
my_output.SetMode('steps')




scheduler.Run(steps=25000)

print "Done!"
