#! /usr/bin/env python
"""

"""
import pdb
import os
import sys

os.environ['NEUROSPACES_NMC_MODELS']='/usr/local/neurospaces/models/library'

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

my_model_container.Load('tests/cells/purk_test_segment.ndf')

#
# Must create solver.
#
my_heccer = scheduler.CreateSolver('My solver', 'heccer')

# Sets the segment of the model to run from
my_heccer.SetModelName('/purk_test_segment')


#
# Create an perfectclamp input object
#
my_perfect_clamp = scheduler.CreateInput('My Injection', 'perfectclamp')

my_perfect_clamp.AddInput('/purk_test_segment/segments/test_segment', 'INJECT')

my_perfect_clamp.SetCommandVoltage(2e-9)


#
# Create Outputs
#
my_output = scheduler.CreateOutput('My output object', 'double_2_ascii')

my_output.AddOutput('/purk_test_segment/segments/test_segment', 'Vm')
my_output.AddOutput('/purk_test_segment/segments/test_segment/cat/cat_gate_activation', 'state_m')
my_output.AddOutput('/purk_test_segment/segments/test_segment/cat/cat_gate_inactivation', 'state_h')
my_output.AddOutput('/purk_test_segment/segments/test_segment/kdr', 'state_m')
my_output.AddOutput('/purk_test_segment/segments/test_segment/kdr', 'state_h')
my_output.AddOutput('/purk_test_segment/segments/test_segment/nap', 'state_n')
my_output.AddOutput('/purk_test_segment/segments/test_segment/naf', 'state_m')
my_output.AddOutput('/purk_test_segment/segments/test_segment/naf', 'state_h')

scheduler.Run(time=0.1)

