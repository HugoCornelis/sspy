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

my_model_container.Load('tests/cells/purk_test.ndf')

my_model_container.SetParameter('/purk_test/segments/soma',
                                'INJECT',
                                2e-09)

#
# Must create solver.
#
my_heccer = scheduler.CreateSolver('My solver', 'heccer', verbose=True)

# Sets the segment of the model to run from
my_heccer.SetModelName('/purk_test')

# set the timestep for the entire scheduler (solvers, inputs and outputs)
my_heccer.SetTimeStep(2e-05)


#
# Create Outputs
#
my_output = scheduler.CreateOutput('My output object', 'double_2_ascii')

my_output.SetFilename('/tmp/output')

my_output.AddOutput('/purk_test/segments/soma', 'Vm')
my_output.AddOutput('/purk_test/segments/soma/ca_pool', 'Ca')
my_output.AddOutput('/purk_test/segments/soma/km', 'state_n')
my_output.AddOutput('/purk_test/segments/soma/kdr', 'state_m')
my_output.AddOutput('/purk_test/segments/soma/kdr', 'state_h')
my_output.AddOutput('/purk_test/segments/soma/ka', 'state_m')
my_output.AddOutput('/purk_test/segments/soma/ka', 'state_h')
my_output.AddOutput('/purk_test/segments/soma/kh', 'state_m')
my_output.AddOutput('/purk_test/segments/soma/kh', 'state_h')
my_output.AddOutput('/purk_test/segments/soma/nap', 'state_n')
my_output.AddOutput('/purk_test/segments/soma/naf', 'state_m')
my_output.AddOutput('/purk_test/segments/soma/naf', 'state_h')
my_output.AddOutput('/purk_test/segments/soma/cat/cat_gate_activation', 'state_m')
my_output.AddOutput('/purk_test/segments/soma/cat/cat_gate_activation', 'state_h')
my_output.AddOutput('/purk_test/segments/main[0]', 'Vm')
my_output.AddOutput('/purk_test/segments/main[0]/ca_pool', 'Ca')
my_output.AddOutput('/purk_test/segments/main[0]/cat/cat_gate_activation', 'state_m')
my_output.AddOutput('/purk_test/segments/main[0]/cat/cat_gate_inactivation', 'state_h')
my_output.AddOutput('/purk_test/segments/main[0]/cap/cap_gate_activation', 'state_m')
my_output.AddOutput('/purk_test/segments/main[0]/cap/cap_gate_inactivation', 'state_h')
my_output.AddOutput('/purk_test/segments/main[0]/km', 'state_n')
my_output.AddOutput('/purk_test/segments/main[0]/kdr', 'state_m')
my_output.AddOutput('/purk_test/segments/main[0]/kdr', 'state_h')
my_output.AddOutput('/purk_test/segments/main[0]/ka', 'state_m')
my_output.AddOutput('/purk_test/segments/main[0]/ka', 'state_h')
my_output.AddOutput('/purk_test/segments/main[0]/kc', 'state_m')
my_output.AddOutput('/purk_test/segments/main[0]/kc', 'state_h')
my_output.AddOutput('/purk_test/segments/main[0]/k2', 'state_m')
my_output.AddOutput('/purk_test/segments/main[0]/k2', 'state_h')


from sspy.save import Save

sspy_save = Save(scheduler)

sspy_save.SaveToFile()

print "Done!"
