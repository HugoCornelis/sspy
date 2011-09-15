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
					      '--shell',
					      '<',
					      '$::config->{core_directory}/tests/python/purk_test.sh',
					     ],
				command => './sspy.py',
				disabled => 'Test confirmed to work manually but refuses to complete',

				command_tests => [
						  {
						   description => "Wait for output",
						   wait => 5,
						
						  },

						  {
						   description => "Do we get the same output from shell (batch file) as from specification and api ?",
						   read => {
							    application_output_file => "/tmp/OutputGenerator",
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
       description => "Purk test run from the shell using a batch file",
       name => 'purk_test_shell.t',
      };


return $test;


