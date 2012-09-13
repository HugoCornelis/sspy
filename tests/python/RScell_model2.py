#! /usr/bin/env python
"""
    simplecell-test.py - test of the simplecell model

    Basic Python script to load a cell model NDF file, provide current
    injection to the soma, and run the simulation, writing the soma Vm to
    a specified file.
"""
import pdb
import os
import sys

class Model():
    def __init__(self):

      # This sets an environment to find the libraries needed for running SSPy
      # It will likely not be required in later versions of G-3

      sys.path.append( os.path.join(os.environ['HOME'],
        'neurospaces_project/sspy/source/snapshots/0/tests/python'))

      # The location of model files to be loaded
      os.environ['NEUROSPACES_NMC_MODELS']= os.path.join('/', 'usr', 'local',
        'neurospaces', 'models', 'library')

      # The following four commands set up SSPy as the scheduler component

      from test_library import add_sspy_path
      add_sspy_path()
      from sspy import SSPy 
      self.scheduler = SSPy(verbose=True)

      # Create a model container service and load an ndf file
      # needed to initialize the model container ???
      self.my_model_container = None    
      self.my_model_container = self.scheduler.CreateService(name="My Model Container",
        type="model_container", verbose=True)

      # The commands above are common to most G-3 Python simulation scripts

      # load a particular NDF cell model file
      self.my_model_container.Load('cells/RScell-nolib.ndf')

      # set a model parameter, the INJECT field to provide constant current injection
      self.my_model_container.SetParameter('/cell/soma', 'INJECT', 0.5e-09)

      # Create a solver, in this case heccer
      my_heccer = self.scheduler.CreateSolver('My solver', 'heccer', verbose=True)

      # Sets the segment (???) of the model to run from
      my_heccer.SetModelName('/cell')

      # set the timestep for the entire scheduler (solvers, inputs and outputs)
      my_heccer.SetTimeStep(2e-05)

      # Create Outputs
      my_output = self.scheduler.CreateOutput('My output object', 'double_2_ascii')
      my_output.SetFilename('RScell_Vm')

      # this adds to output to the output object
      my_output.AddOutput('/cell/soma', 'Vm')

      # Optionally, provide output a multiple of the simulation time step
      my_output.SetResolution(5)

    def run_simulation(self,simulationtime):
        self.scheduler.Run(time=simulationtime, finish=False)

    def set_injection(self, injection):
        self.my_model_container.SetParameter('/cell/soma', 'INJECT', injection)
4
# Main program, executes a simulation with
# with 0.5 seconds.
#
if __name__ == '__main__':
    myModel = Model()
    # run with default 0.5e-9 injection
    myModel.run_simulation(0.5)
    # reset and run again with 0.7e-9 injection
    myModel.scheduler.Reset()
    myModel.set_injection(0.7e-9)
#    myModel.run_simulation(0.5)
    myModel.scheduler.Run(time=0.5, finish=False)
