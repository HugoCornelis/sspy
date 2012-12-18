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
					      "--verbose",
					      "$::config->{core_directory}/yaml/purk_test_soma_aggregators.yml",
					     ],
				command => './sspy.py',
				command_tests => [

						  {
						   description => "Check for script completion",
						   read => 'Loading schedule \'yaml/purk_test_soma_aggregators.yml\'
Parsing schedule data
Schedule name is \'purk_test_soma\'

Loading model from file \'tests/cells/purk_test_soma.ndf\'
Loading Service \'purk_test_soma (model_container)\' of type \'model_container\'
Loading Solver \'purk_test_soma (heccer)\' of type \'heccer\'

Found applied simulation parameters:
Simulation Parameters: 
	Simulation will run for 5000 steps
	Verbosity level is 1

Loading Output \'purk_test_soma (double_2_ascii)\' of type \'double_2_ascii\'


Applying model runtime parameters to 1 models
	Setting runtime parameters for \'/purk_test_soma\'
	Setting model name for solver \'purk_test_soma (heccer)\' to \'/purk_test_soma\'
Model Container: setting parameter /purk_test_soma/segments/soma INJECT 2e-09


Connecting 1 solvers to 1 services
	Connecting solver \'purk_test_soma (heccer)\' to service \'purk_test_soma (model_container)\'




Compiling all solvers
	Compiling Solver: purk_test_soma (heccer)




Connecting 1 outputs to 1 solvers
	Connecting solvers to output \'purk_test_soma (double_2_ascii)\'




Scheduling all simulation objects
	Scheduling solvers:
		Scheduling solver \'purk_test_soma (heccer)\'
	Scheduling outputs:
		Scheduling output \'purk_test_soma (double_2_ascii)\'


Initializing all schedulees
	Initializing Schedulee: purk_test_soma (heccer)
	Initializing Schedulee: purk_test_soma (double_2_ascii)


Running simulation in steps mode
Finishing simulation
',
						   timeout => 50,
						  },
						  {
						   description => "Is the purkinje cell soma solved correctly, with aggregators ?",
						   read => {
							    application_output_file => "/tmp/purk_test_soma_aggregators",
							    expected_output_file => "$::config->{core_directory}/tests/specifications/strings/purk_test_soma_aggregators.txt",
							   },
						   wait => 5,
						  },
						 ],
				description => "Test a segment from the purkinje cell soma with aggregators from declaration",
				preparation => {
						description => "Clean out any previous files",
						preparer =>
						sub
						{
						    `rm -f /tmp/purk_test_soma_aggregators`;
						},
					       },
				reparation => {
					       description => "Remove the generated output files",
					       reparer =>
					       sub
					       {
 						   `rm -f /tmp/purk_test_soma_aggregators`;
					       },
					      },

			       },


			       {
				arguments => [
					     ],
				command => 'tests/python/purk_test_soma_aggregators_api.py',
				command_tests => [
						  {
						   description => "Check for script completion",
						   read => 'Done!',
						   timeout => 10,
						  },

						  {
						   description => "Is the purkinje cell soma solved correctly, with aggregators via API ?",
						   read => {
							    application_output_file => "/tmp/purk_test_soma_aggregators",
							    expected_output_file => "$::config->{core_directory}/tests/specifications/strings/purk_test_soma_aggregators.txt",
							   },
						   timeout => 10,
						  },
						 ],
				description => "Test a segment of the purkinje cell some with aggregators from api",
				preparation => {
						description => "Clean out any previous files",
						preparer =>
						sub
						{
						    `rm -f /tmp/purk_test_soma_aggregators`;
						},
					       },
				reparation => {
					       description => "Remove the generated output files",
					       reparer =>
					       sub
					       {
 						   `rm -f /tmp/purk_test_soma_aggregators`;
					       },
					      },

			       },
			      ],
       description => "Purkinje test soma with aggregators",
       name => 'purk_test_soma_aggregators.t',
      };


return $test;


