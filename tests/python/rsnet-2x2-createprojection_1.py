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

# we go one layer lower below the plugin layer so that we
# can do work on the model container core.
my_mc_object = my_model_container.GetObject()

#pdb.set_trace()
my_mc_object.NDFLoadLibrary('cells/RScell-nolib2.ndf', 'rscell')

nx= 2 # number of cells nx*ny
ny=2

sep_x= 0.002 # 2mm
sep_y=0.002
sep_z=1.0e-6 # give it a tiny z range in case of round off errors

syn_weight=10
cond_vel=0.5
prop_delay=sep_x / cond_vel

my_mc_object.CreateNetwork('/RSNet')

my_mc_object.CreateMap('::rscell::/cell', '/RSNet/population', nx, ny, sep_x, sep_y)


my_mc_object.CreateProjection(network='/RSNet',
                            projection='/RSNet/projection',
                            probability=1.0,
                            random_seed=1212.0,
                            source=('/RSNet/population', 'box', -1e10, -1e10, -1e10, 1e10, 1e10, 1e10),
                            target=('/RSNet/population', 'Ex_channel', 0, 0, 0, sep_x * 1.2, sep_y * 1.2, sep_z * 0.5),
                            target_hole=('box', sep_x *0.5, sep_y * 0.5, sep_z * 0.5, sep_x * 05, sep_y * 0.5, sep_z * 0.5),
                            synapse=('fixed', prop_delay, syn_weight, 0.5, 'spike', 'Ex_channel')
                            )



# Create a perfectclamp object for current holding.
my_input = scheduler.CreateInput('My perfectclamp','perfectclamp',verbose=True)

my_input.AddInput('/RSNet/population/3/soma', 'INJECT')

my_input.SetCommandVoltage(1e-9)



#
# Must create solver.
#
# my_heccer = scheduler.CreateSolver('My heccer', 'heccer', verbose=True)

# # Sets the segment of the model to run from
# my_heccer.SetModelName('/RSNet')

# # set the timestep for the entire scheduler (solvers, inputs and outputs)
# my_heccer.SetTimeStep(2e-05)


#
# Must a des.
#
my_des = scheduler.CreateEventDistributor('My DES', 'des', verbose=True)

my_des.SetModelName('/RSNet')


for i in range(0, nx*ny):

    path = "/RSNet/population/%s" % i

    # This performs a lookup and set on the solver by the solver name
    # given when you create it via CreateSolver.

    scheduler.SolverSet(path, 'My heccer')




#
# Create Outputs
#
my_output = scheduler.CreateOutput('My output object', 'double_2_ascii')

my_output.SetFilename('/tmp/output')

for i in range(0, nx * ny):

    my_output.AddOutput("/RSNet/population/%s/soma" % i, 'Vm')

    my_output.AddOutput("/RSNet/population/%s/soma/Ex_channel" % i, 'Gsyn')


# This should probably just be arg flags or something, passing 'steps'
# seems a bit tacky.
my_output.SetMode('steps')

my_output.SetResolution(10)





scheduler.SetModelName('/RSNet')

scheduler.Run(time=0.2)

print "Done!"
