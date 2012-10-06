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

# we go one layer lower below the plugin layer so that we
# can do work on the model container core.
my_mc_core = my_model_container.GetCore()


my_mc_core.NDFLoadLibrary('cells/RScell-nolib.ndf', 'rscell')

nx= 2 # number of cells nx*ny
ny=2

sep_x= 0.002 # 2mm
sep_y=0.002
sep_z=1.0e-6 # give it a tiny z range in case of round off errors

syn_weight=10
cond_vel=0.5
prop_delay=sep_x / cond_vel

my_mc_core.CreateNetwork('/RSNet')

my_mc_core.CreateMap('::rscell::/cell', '/RSNet/population', nx, ny, sep_x, sep_y)


my_mc_core.CreateProjection(network='/RSNet',
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
my_heccer = scheduler.CreateSolver('My solver', 'heccer', verbose=True)

# Sets the segment of the model to run from
my_heccer.SetModelName('/RSNet')

# set the timestep for the entire scheduler (solvers, inputs and outputs)
my_heccer.SetTimeStep(2e-05)



##########
# user workflow: configure the simulation

# configure the numerical solver

heccer_set_config('disassem_simple');

set_verbose('debug');

ce('/RSNet/population');

for (my $counter = 0 ; $counter < $NX * $NY ; $counter++)
{
    solverset($counter, 'heccer', '/RSNet');
}

solverset('/RSNet/projection', 'des', '/RSNet');

# save the schedule for later use

ssp_save('/RSNet', '/tmp/network-simple.ssp');



##########
# user workflow: run the simulation

# run the simulation

run('/RSNet', '0.2');
---------------------------------------



ce('/RSNet/population');

for (my $counter = 0 ; $counter < $NX * $NY ; $counter++)
{
    output_add($counter . '/soma', 'Vm');
}

for (my $counter = 0 ; $counter < $NX * $NY ; $counter++)
{
    output_add($counter . '/soma/Ex_channel', 'Gsyn');
}

#
# Create Outputs
#
my_output = scheduler.CreateOutput('My output object', 'double_2_ascii')

my_output.SetFilename('/tmp/output')

counter = 0

while counter < NX * NY:

    my_output.AddOutput("/RSNet/population/%s/soma" % counter, 'Vm')

    my_output.AddOutput("/RSNet/population/%s/soma/Ex_channel" % counter, 'Gsyn')

    counter += 1


# This should probably just be arg flags or something, passing 'steps'
# seems a bit tacky.
my_output.SetMode('steps')

my_output.SetResolution(10)



scheduler.Run(time=0.2)

print "Done!"