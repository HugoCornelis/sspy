#! /usr/bin/env python
"""
    cal1_api.py - test of loading and running the cal1.ndf model
"""
import pdb   # the Python debugger
import os
import sys

# The commands below are common to most G-3 Python simulation scripts

# This sets an environment to find the libraries needed for running SSPy
# It will likely not be required in later versions of G-3
sys.path.append( os.path.join(os.environ['HOME'],
         'neurospaces_project/sspy/source/snapshots/0/tests/python'))

# The location of model files to be loaded
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

my_model_container.Load('chemesis/cal2.ndf')

#
# Must create solver.
#
my_chemesis3 = scheduler.CreateSolver('My Chemesis3', 'chemesis3')

# Sets the element of the model to run from
my_chemesis3.SetModelName('/cal2')

# set the timestep for the entire scheduler (solvers, inputs and outputs)
my_chemesis3.SetTimeStep(0.002)

#
# Create Outputs
#
cal_output = scheduler.CreateOutput('cal output object', 'double_2_ascii')
buf_output = scheduler.CreateOutput('buf output object', 'double_2_ascii')

cal_output.SetFilename('cal2_cal.txt')
buf_output.SetFilename('cal2_buf.txt')

cal_output.SetResolution(50)
buf_output.SetResolution(50)

cal_output.AddOutput('/cal2/soma/cal1/Ca', 'concentration')
cal_output.AddOutput('/cal2/dend/cal1/Ca', 'concentration')

buf_output.AddOutput('/cal2/soma/cal1/Cabuf', 'concentration')
buf_output.AddOutput('/cal2/dend/cal1/Cabuf', 'concentration')

scheduler.Run(steps=500000)

print "Done!"
