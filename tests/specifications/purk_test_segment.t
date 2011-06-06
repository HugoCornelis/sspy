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
				command => 'tests/python/purk_test_segment.py',
				command_tests => [
						  {
						   description => "Check for script completion",
						   read => 'Done!',
						   timeout => 10,
						  },
						  {
						   description => "Can we test a segment of the purkinje cell by loading it from a declarative specification ?",
						   read => {
							    application_output_file => "/tmp/OutputGenerator",
							    expected_output_file => "$::config->{core_directory}/tests/specifications/strings/purk_test_segment.txt",
							   },
						  },
						 ],
				description => "Test a segment from the purkinje cell from declaration",
				preparation => {
						description => "Clean out any previous files",
						preparer =>
						sub
						{
						    `rm -f /tmp/OutputGenerator`;
						},
					       },
				reparation => {
					       description => "Remove the generated output files",
					       reparer =>
					       sub
					       {
 						   `rm -f /tmp/OutputGenerator`;
					       },
					      },

			       },


			       {
				arguments => [
					     ],
				command => 'tests/python/purk_test_segment_api.py',
				command_tests => [
						  {
						   description => "Check for script completion",
						   read => 'Done!',
						  },
						  {
						   description => "Can we test a segment of the purkinje cell by creating it via API ?",
						   read => {
							    application_output_file => "/tmp/OutputGenerator",
							    expected_output_file => "$::config->{core_directory}/tests/specifications/strings/purk_test_segment.txt",
							   },
						  },
						 ],
				description => "Test a segment of the purkinje cell from api",
				preparation => {
						description => "Clean out any previous files",
						preparer =>
						sub
						{
						    `rm -f /tmp/OutputGenerator`;
						},
					       },
				reparation => {
					       description => "Remove the generated output files",
					       reparer =>
					       sub
					       {
 						   `rm -f /tmp/OutputGenerator`;
					       },
					      },

			       },
			      ],
       description => "Purkinje test segment",
       name => 'purk_test_segment.t',
      };


return $test;


