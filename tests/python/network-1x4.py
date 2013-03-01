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

my_mc_object.SetParameter('::rscell::/cell/soma/Ex_channel', 'G_MAX', '0.04330736624')
my_mc_object.SetParameter('::rscell::/cell/soma/Ex_channel', 'Erev', '0')

my_mc_object.Create('/n_cells', 'network')
pdb.set_trace()

my_mc_object.InsertAlias('::rscell::/cell', '/n_cells/s1')
my_mc_object.InsertAlias('::rscell::/cell', '/n_cells/t1')
my_mc_object.InsertAlias('::rscell::/cell', '/n_cells/t2')
my_mc_object.InsertAlias('::rscell::/cell', '/n_cells/t3')
my_mc_object.InsertAlias('::rscell::/cell', '/n_cells/t4')

my_mc_object.Create('/n_cells/projection', 'projection')
pdb.set_trace()


my_mc_object.SetParameter('/n_cells/projection', 'SOURCE', '/n_cells')
my_mc_object.SetParameter('/n_cells/projection', 'TARGET', '/n_cells')


my_mc_object.Create('/n_cells/projection/1', 'single_connection')
pdb.set_trace()

my_mc_object.SetParameter('/n_cells/projection/1', 'PRE', 's1/soma/spike')
my_mc_object.SetParameter('/n_cells/projection/1', 'POST', 't1/soma/Ex_channel/synapse')
my_mc_object.SetParameter('/n_cells/projection/1', 'WEIGHT', '2.0')
my_mc_object.SetParameter('/n_cells/projection/1', 'DELAY', '0.03')



my_mc_object.Create('/n_cells/projection/2', 'single_connection')
my_mc_object.SetParameter('/n_cells/projection/2', 'PRE', 's1/soma/spike')
my_mc_object.SetParameter('/n_cells/projection/2', 'POST', 't2/soma/Ex_channel/synapse')
my_mc_object.SetParameter('/n_cells/projection/2', 'WEIGHT', '1.0')
my_mc_object.SetParameter('/n_cells/projection/2', 'DELAY', '0.02')


my_mc_object.Create('/n_cells/projection/3', 'single_connection')
my_mc_object.SetParameter('/n_cells/projection/3', 'PRE', 's1/soma/spike')
my_mc_object.SetParameter('/n_cells/projection/3', 'POST', 't3/soma/Ex_channel/synapse')
my_mc_object.SetParameter('/n_cells/projection/3', 'WEIGHT', '0.1')
my_mc_object.SetParameter('/n_cells/projection/3', 'DELAY', '2')

my_mc_object.Create('/n_cells/projection/4', 'single_connection')
my_mc_object.SetParameter('/n_cells/projection/4', 'PRE', 's1/soma/spike')
my_mc_object.SetParameter('/n_cells/projection/4', 'POST', 't4/soma/Ex_channel/synapse')
my_mc_object.SetParameter('/n_cells/projection/4', 'WEIGHT', '10.0')
my_mc_object.SetParameter('/n_cells/projection/4', 'DELAY', '0.02')




#scheduler.SetTimeStep(2e-05)

#scheduler.Run(time=0.2)

print "Done!"
