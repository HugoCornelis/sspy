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

my_model_container.Load('cells/purkinje/edsjb1994.ndf')


#
# Must create solver.
#
my_heccer = scheduler.CreateSolver('My solver', 'heccer', verbose=True)

# Not sure wether to give this a get/set method 
my_heccer.options = 4

my_heccer.SetGranularity(1)

# Sets the segment of the model to run from
my_heccer.SetModelName('/Purkinje')

# set the timestep for the entire scheduler (solvers, inputs and outputs)
my_heccer.SetTimeStep(0.5)


#
# Create a pulsegen object for current holding.
#
my_pulsegen = scheduler.CreateInput('purkinje cell perfect clamp','pulsegen',verbose=True)

my_pulsegen.AddInput('/Purkinje/segments/soma', 'Vm')

my_pulsgen.level1 = 50.0
my_pulsgen.width1 = 3.0
my_pulsgen.delay1 = 5.0
my_pulsgen.level2 = -20.0
my_pulsgen.width2 = 5.0
my_pulsgen.delay2 = 8.0
my_pulsgen.baselevel = 10.0
my_pulsgen.triggermode = 0 # zero is "free run"


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




scheduler.Run(steps=200)

print "Done!"
