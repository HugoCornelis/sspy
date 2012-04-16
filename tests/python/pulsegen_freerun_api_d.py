#! /usr/bin/env python
"""

"""
import pdb
import os
import sys

# This sets an environment to find the libraries needed for running SSPy
# It will likely not be required in later versions of G-3

sys.path.append( os.path.join(os.environ['HOME'],
    'neurospaces_project/sspy/source/snapshots/0/tests/python'))


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
my_heccer.SetTimeStep(2e-05)


#
# Create a pulsegen object for current holding.
#
my_pulsegen = scheduler.CreateInput('pulsegen','pulsegen',verbose=True)


my_pulsegen.AddInput('/Purkinje/segments/soma', 'INJECT')

my_pulsegen.baselevel = 0.0
my_pulsegen.level1 = 0.5e-09

my_pulsegen.delay1 = 0.05
my_pulsegen.width1 = 0.15
my_pulsegen.level2 = 0.0
my_pulsegen.width2 = 0.0
my_pulsegen.delay2 = 100.0 # give it a very long delay to prevent repeating

my_pulsegen.triggermode = 0 # zero is "free run"


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
