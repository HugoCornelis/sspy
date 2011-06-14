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
					      "$::config->{core_directory}/tests/yaml/purk_test_soma.yml",
					     ],
				command => './sspy',
				command_tests => [
						  {
						   description => "Check for script completion",
						   read => 'Finishing simulation',
						   timeout => 80,
						  },
						  {
						   description => "Is the purkinje cell soma solved correctly, no aggregators ?",
						   read => {
							    application_output_file => "/tmp/OutputGenerator",
							    expected_output_file => "$::config->{core_directory}/tests/specifications/strings/purk_test_soma.txt",
							   },
						  },
						 ],
				description => "Test a soma from the purkinje cell from declaration",
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
				command => 'tests/python/purk_test_soma_api.py',
				command_tests => [
						  {
						   description => "Check for script completion",
						   read => 'Done!',
						   timeout => 50,
						  },
						  {
						   description => "Is the purkinje cell soma solved correctly from API, no aggregators ?",
						   read => {
							    application_output_file => "/tmp/OutputGenerator",
							    expected_output_file => "$::config->{core_directory}/tests/specifications/strings/purk_test_soma.txt",
							   },
						  },
						 ],
				description => "Test a soma of the purkinje cell from api",
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
       description => "Purkinje test soma",
       name => 'purk_test_soma.t',
      };


return $test;


