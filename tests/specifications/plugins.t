#!/usr/bin/perl -w
#

use strict;


my $test
    = {
       command_definitions => [

			       {
				arguments => [
					     ],
				command => 'tests/python/add_solver_plugins.py',
				command_tests => [
						  {
						   disabled => "disabled due to an ordering error",
						   description => "Can we load some solver plugins from the top level of sspy ?",

						   read => "printing the currently loaded solvers
solver plugins:

heccer

Loading test solver 'test'
Loading test solver 'test 2'
printing loaded solver plugins after dynamically loading
solver plugins:

heccer
test
test 2
",

						  },
						 ],
				description => "Loads test solver plugins in addition to the ones present in sspy.",
			       },



			       {
				arguments => [
					     ],
				command => 'tests/python/add_service_plugins.py',
				command_tests => [
						  {
						   disabled => "disabled due to an ordering error",

						   description => "Can we load some service plugins from the top level of sspy ?",

						   read => "printing the currently loaded services
service plugins:

heccer_intermediary
model_container

Loading test service 'test'
Loading test service 'test 2'
printing loaded service plugins after dynamically loading
service plugins:

heccer_intermediary
model_container
test
test 2
",

						  },
						 ],
				description => "Loads test service plugins in addition to the ones present in sspy.",
			       },

			      ],
       description => "Tests sspy's ability to load plugins from files and directories.",
       name => 'plugins.t',
      };


return $test;


