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
				command => 'tests/python/purk_test.py',
				command_tests => [
						  {
						   description => "Check for script completion",
						   read => 'Done!',
						   timeout => 100,
						  },
						  {
						   description => "Can we test the purkinje cell by loading it from a declarative specification ?",
						   read => {
							    application_output_file => "/tmp/output",
							    expected_output_file => "$::config->{core_directory}/tests/specifications/strings/purk_test.txt",
							   },
						  },
						 ],
				description => "Test a segment from the purkinje cell from declaration",
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


			       {
				arguments => [
					     ],
				command => 'tests/python/purk_test_api.py',
				command_tests => [
						  {
						   description => "Check for script completion",
						   read => 'Done!',
						   timeout => 50,
						  },
						  {
						   description => "Can we test the purkinje cell by creating it via API ?",
						   read => {
							    application_output_file => "/tmp/output",
							    expected_output_file => "$::config->{core_directory}/tests/specifications/strings/purk_test.txt",
							   },
						  },
						 ],
				description => "Test a segment of the purkinje cell from api",
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
       description => "Purkinje test segment",
       name => 'purk_test.t',
      };


return $test;


