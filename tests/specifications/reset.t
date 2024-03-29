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
				command => 'tests/python/reset1.py',
				command_tests => [
						  {
						   description => "Check for script completion",
						   read => 'Done!',
						   timeout => 10,
						  },
						  {
						   description => "Can we perform a simple reset on a single passive compartment with output appending ?",
						   read => {
							    application_output_file => "/tmp/output",
							    expected_output_file => "$::config->{core_directory}/tests/specifications/strings/reset1.txt",
							   },
						  },
						 ],
				description => "Can we perform a reset on a simple model via API",
				timeout => 10,
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
				command => 'tests/python/reset2.py',
				command_tests => [
						  {
						   description => "Check for script completion",
						   read => 'Done!',
						   timeout => 10,
						  },
						  {
						   description => "Can we perform a reset on a single compartment without appending to output ?",
						   read => {
							    application_output_file => "/tmp/output",
							    expected_output_file => "$::config->{core_directory}/tests/specifications/strings/reset2.txt",
							   },
						  },
						 ],
				description => "Can we perform a reset on a simple model via API",
				timeout => 10,
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
				command => 'tests/python/reset3.py',
				command_tests => [
						  {
						   description => "Check for script completion",
						   read => 'Done!',
						   timeout => 10,
						  },
						  {
						   description => "Can we perform a simple reset on a single passive compartment with output appending and perfectclamp ?",
						   read => {
							    application_output_file => "/tmp/output",
							    expected_output_file => "$::config->{core_directory}/tests/specifications/strings/reset3.txt",
							   },
						  },
						 ],
				description => "Can we perform a reset on a simple model via API",
				timeout => 10,
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
				command => 'tests/python/reset4.py',
				command_tests => [
						  {
						   description => "Check for script completion",
						   read => 'Done!',
						   timeout => 10,
						  },
						  {
						   description => "Can we perform a reset on a single compartment without appending to output with perfectclamp ?",
						   read => {
							    application_output_file => "/tmp/output",
							    expected_output_file => "$::config->{core_directory}/tests/specifications/strings/reset4.txt",
							   },
						  },
						 ],
				description => "Can we perform a reset on a simple model via API",
				timeout => 10,
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
       description => "Reset test",
       name => 'reset.t',
      };


return $test;


