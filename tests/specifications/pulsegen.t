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
				command => 'tests/python/pulsegen_freerun_api.py',
				command_tests => [
						  {
						   disabled => "Simulation takes too long to be practical",
						   description => "Check for script completion",
						   read => 'Done!',
						   timeout => 150,
						  },
						  {
						   disabled => "Simulation takes too long",
						   description => "Can we test the pulsegen in freerun mode by creating it via API ?",
						   read => {
							    application_output_file => "/tmp/output",
							    expected_output_file => "$::config->{core_directory}/tests/specifications/strings/pulsegen_freerun.txt",
							   },
						  },
						 ],
				description => "Test a segment of the pulsegen freerun from api",
				preparation => {
						description => "Clean out any previous files",
						preparer =>
						sub
						{
						    `rm -f /tmp/output`;
						},
					       },
				reparation => {
					       description => "Remove the generated output files",
					       reparer =>
					       sub
					       {
 						   `rm -f /tmp/output`;
					       },
					      },

			       },

			      ],
       description => "Pulsegen tests",
       name => 'pulsegen.t',
      };


return $test;


