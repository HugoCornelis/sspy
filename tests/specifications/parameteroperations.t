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
					     ],
				command => 'tests/python/parameter_operation_1.py',
				command_tests => [
						  {
						   description => "Can we retrieve the INJECT parameter from the scheduler ?",
						   read => 'INJECT value before run prepare is: 2e-09
INJECT value after run prepare is: 2e-09
Done!
',


						  },
						 ],
				description => "Returns the INJECT value that is set via script",
				timeout => 15,
			       },




			       {
				arguments => [
					     ],
				command => 'tests/python/parameter_operation_2.py',
				command_tests => [
						  {
						   description => "Can we check parameters on an element ?",
						   read => '
Parameters on \'/purk_test/segments/soma\' before compile
DIA: 2.98e-05
LENGTH: 0.0
INJECT: 2e-09
rel_Y: 0.0
rel_X: 0.0
rel_Z: 0.0

Parameters on \'/purk_test/segments/soma\' after compile
DIA: 2.98e-05
SURFACE: 2.78985994009e-09
Vm: -0.068
LENGTH: 0.0
INJECT: 2e-09
rel_Y: 0.0
rel_X: 0.0
rel_Z: 0.0

Done!
',


						  },
						 ],
				description => "prints out the parameter values for an element in the purk_test model",
				timeout => 15,
			       },


			      ],
       description => "Some test for setting and retrieving parameters",
       name => 'parameteroperations.t',
      };


return $test;


