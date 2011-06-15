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
				command => 'tests/python/output1.py',
				command_tests => [
						  {
						   description => "Check for script completion",
						   read => 'Done!',
						   timeout => 15,
						  },
						  {
						   description => "Can we produce simple output with simulation time?",
						   read => {
							    application_output_file => "/tmp/output",
							    expected_output_file => "$::config->{core_directory}/tests/specifications/strings/output1.txt",
							   },
						  },
						 ],
				description => "simple output with simulation time",
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
				command => 'tests/python/output2.py',
				command_tests => [
						  {
						   description => "Check for script completion",
						   read => 'Done!',
						  },
						  {
						   description => "Can we produce simple output with the steps mode?",
						   read => {
							    application_output_file => "/tmp/output",
							    expected_output_file => "$::config->{core_directory}/tests/specifications/strings/output2.txt",
							   },
						  },
						 ],
				description => "simple output with the steps mode",
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
				command => 'tests/python/output3.py',
				command_tests => [
						  {
						   description => "Check for script completion",
						   read => 'Done!',
						   timeout => 5,
						  },
						  {
						   description => "Can we produce output with the steps mode at a coarser resolution?",
						   read => {
							    application_output_file => "/tmp/output",
							    expected_output_file => "$::config->{core_directory}/tests/specifications/strings/output3.txt",
							   },
						   wait => 3,

						  },
						 ],
				description => "output with the steps mode at a coarser resolution",
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
				command => 'tests/python/output4.py',
				command_tests => [
						  {
						   description => "Check for script completion",
						   read => 'Done!',
						   timeout => 5,
						  },
						  {
						   description => "Can we produce simple output with the steps mode and a format field?",
						   read => {
							    application_output_file => "/tmp/output",
							    expected_output_file => "$::config->{core_directory}/tests/specifications/strings/output4.txt",
							   },
						   wait => 3,

						  },
						 ],
				description => "simple output with the steps mode and a format field",
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
       description => "output functions",
       name => 'output.t',
      };


return $test;


