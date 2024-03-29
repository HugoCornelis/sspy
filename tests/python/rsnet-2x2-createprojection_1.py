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
                            target=('/RSNet/population', 'ellipse', 0, 0, 0, sep_x * 1.2, sep_y * 1.2, sep_z * 0.5),
                            target_hole=('box', -sep_x *0.5, -sep_y * 0.5, -sep_z * 0.5, sep_x * 0.5, sep_y * 0.5, sep_z * 0.5),
                            synapse=('spike', 'Ex_channel', syn_weight, prop_delay)
                            )



# Create a perfectclamp object for current holding.
my_input = scheduler.CreateInput('My perfectclamp','perfectclamp')


# Here we give it a solver argument to tell the input that the path '/RSNet/population/3/soma'
# is located on the solver 'heccer_3'. if we leave this off then it will search
# through all given solvers and add it to the first that returns an address
# (Note that will work with this example).
# this can cause problems if several solvers possible map to the same pathname.
my_input.AddInput('/RSNet/population/3/soma', 'INJECT', solver='heccer_3')

my_input.SetCommand(1e-9)




#
# Must a des.
#
my_des = scheduler.CreateEventDistributor('My DES', 'des')

my_des.SetModelName('/RSNet')


for i in range(0, nx*ny):

    path = "/RSNet/population/%s" % i

    solver_name = "heccer_%s" % i

    # Here we create a solver with the solver name being heccer_<id number>

    this_heccer = scheduler.CreateSolver(solver_name, 'heccer')

    this_heccer.SetModelName(path)

    # This works but I'm doing it closer to the Run() call down below.
    # this_heccer.SetTimeStep(2e-05)

    # This performs a lookup and set on the solver by the solver name
    # given when you create it via CreateSolver.

    scheduler.SolverSet(path, solver_name)


scheduler.SolverSet("/RSNet/Projection", "My DES")


#
# Create Outputs
#
my_output = scheduler.CreateOutput('My output object', 'double_2_ascii')

my_output.SetFilename('/tmp/output')


# First we add the solver Vm to the first four columns
for i in range(0, nx * ny):

    solver = "heccer_%s" % i

    my_output.AddOutput("/RSNet/population/%s/soma" % i, 'Vm', solver)

# Then we add the Gsyn to the next four
for i in range(0, nx * ny):

    solver = "heccer_%s" % i

    my_output.AddOutput("/RSNet/population/%s/soma/Ex_channel" % i, 'Gsyn', solver)


# This should probably just be arg flags or something, passing 'steps'
# seems a bit tacky.
my_output.SetMode('steps')

# turn off the resolution setting for now
#my_output.SetResolution(10)


scheduler.SetTimeStep(2e-05)

scheduler.Run(time=0.2)

print "Done!"
