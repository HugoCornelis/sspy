#!/usr/bin/perl -w
#

use strict;


my $test
    = {
       command_definitions => [

			       {
				arguments => [
					     ],
				command => 'tests/python/heccer_address_test.py',
				command_tests => [
						  {
						   description => "Can we get and set parameters in heccer?",

						   read => "Model Container: setting parameter /purk_test/segments/soma INJECT 2e-09


No model runtime parameters defined


Connecting 1 solvers to 1 services
	Connecting solver 'My solver' to service 'My Model Container'


Compiling all solvers
	Compiling Solver: My solver






Scheduling all simulation objects
	Scheduling solvers:
		Scheduling solver 'My solver'


Initializing all schedulees
	Initializing Schedulee: My solver


INJECT value is 0.0000000020
Setting '/purk_test/segments/soma'->'INJECT' to 3e-09
INJECT value is 0.0000000030
Done!
",

						  },
						 ],
				description => "Test for seeing if we can get and set a parameter in the solver model intermediary..",
			       },



			       {
				arguments => [
					     ],
				command => 'tests/python/set_parameter_1.py',
				command_tests => [
						  {
						   description => "Can we get and set parameters in heccer?",

						   read => "Model Container: setting parameter /purk_test/segments/soma INJECT 2e-09


No model runtime parameters defined


Connecting 1 solvers to 1 services
	Connecting solver 'My solver' to service 'My Model Container'


Compiling all solvers
	Compiling Solver: My solver






Scheduling all simulation objects
	Scheduling solvers:
		Scheduling solver 'My solver'


Initializing all schedulees
	Initializing Schedulee: My solver


INJECT value is 0.0000000020
Setting '/purk_test/segments/soma'->'INJECT' to 3e-09
INJECT value is 0.0000000030
Done!
",

						  },
						 ],
				description => "Test to see if we can change parameters from the top level of the scheduler API.",
			       },

			      ],
       description => "Checks the heccer addressing capabilities",
       name => 'heccer_addressing.t',
      };


return $test;


