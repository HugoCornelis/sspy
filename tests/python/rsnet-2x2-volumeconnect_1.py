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


my_model_container.NDFLoadLibrary('cells/RScell-nolib2.ndf', 'rscell')

# my_model_container.SetParameter('/RSNet/population/3/soma',
#                                 'INJECT',
#                                 1e-09)


# Here we work one level lower with the model container
# instead of the model container plugin wrapper.
my_mc_object = my_model_container.GetObject()

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


# create projection configuration


config = {'root' : '/RSNet',
          'projection' : { 'name' : '/RSNet/projection',
                           'source': '../population',
                           'target' : '../population',
                           },
          'source' : { 'context' : '/RSNet/population',
                       'include' : { 'type' : 'box',
                                       'coordinates' : [-1e10, -1e10, -1e10, 1e10, 1e10, 1e10],
                                       
                                     },
                       },
                       

          'target' : { 'context' : '/RSNet/population',
                       'include' : { 'type' : 'ellipse',
                                     'coordinates' : [0, 0, 0, sep_x *1.2, sep_y * 1.2, sep_z * 0.5]
                                     },
                       'exclude' : 'destination_hole',
                                   'type' : 'box',
                                   'coordinates' : [sep_x * 0.5, sep_y * 0.5, sep_z * 0.5, sep_x * 0.5, sep_y * 0.5, sep_z * 05],                       
                       
                       },

          'synapse' : { 'pre' : 'spike',
                        'post' : 'Ex_channel',
                        'weight' : { 'weight_indicator' : 'weight',
                                     'weight' : syn_weight,
                                     },
                        'delay' : { 'delay_indicator' : 'delay',
                                    'delay_type' : 'fixed',
                                    'value' : prop_delay,
                                    'velocity' : '',
                                    }
                        
                        },
            'probability' : 1.0,
            'random_seed' : 1212.0
          
          }


my_mc_object.CreateProjection(configuration=config)


#
# Must create solver.
#
my_heccer = scheduler.CreateSolver('My solver', 'heccer', verbose=True)

# Sets the segment of the model to run from
my_heccer.SetModelName('/purk_test_soma')

# Set the reporting granularity
my_heccer.SetGranularity(1000)

# set the timestep for the entire scheduler (solvers, inputs and outputs)
my_heccer.SetTimeStep(5e-06)


#
# Create Outputs
#
my_output = scheduler.CreateOutput('My output object', 'double_2_ascii')

my_output.AddOutput('/purk_test_soma/segments/soma', 'Vm')



scheduler.Run(time=0.2, finish=True)

print "Done!"
