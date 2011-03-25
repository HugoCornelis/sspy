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
				command => 'tests/python/pool1_feedback1.py',
				command_tests => [
						  {
						   description => "Check for script completion",
						   read => 'Done!',
						  },
						  {
						   description => "Is a pool integrated correctly, one compartment, one pool with a feedback loop ?",
						   read => {
							    application_output_file => "/tmp/OutputGenerator",
							    expected_output_file => "$::config->{core_directory}/tests/specifications/strings/pool1_feedback1.txt",
							   },
						  },
						 ],
				description => "pool integration, one compartment, one pool with a feedback loop",
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
       description => "pool integration & related",
       name => 'pools.t',
      };


return $test;


