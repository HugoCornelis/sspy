#!/usr/bin/perl -w
#

use strict;


# slurp mode

local $/;


my $test
    = {
       command_definitions => [
			       {
				arguments => [
					      '--shell'
					     ],
				command => './sspy',
				disabled => 'Due to the prompt appearing in output this test passes on macs but not on linux',
				command_tests => [
						  {
						   description => "List the service plugins",
						   read => 'service plugins:

heccer_intermediary
model_container
',
						   write => 'list_service_plugins',
						  },
						  {
						   description => "List the solver plugins",
						   read => 'solver plugins:

heccer

',
						   write => 'list_solver_plugins',
						  },

						  {
						   description => "List the input plugins",
						   read => 'input plugins:

perfectclamp
pulsegen

',
						   write => 'list_input_plugins',
						  },

						  {
						   description => "List the output plugins",
						   read => 'output plugins:

double_2_ascii

',
						   write => 'list_output_plugins',
						  },
						 ],

			       },

			      ],
       description => "basic shell functionality",
       name => 'shell.t',
      };


return $test;


