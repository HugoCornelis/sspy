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
				command => 'tests/python/edsjb1994-perfectclamp.py',
				diabled => "Can't get outputs to match",
				command_tests => [
						  {
						   description => "Check for script completion",
						   read => 'Done!',
						   timeout => 300,
						  },
						  {
						   description => "Can we clamp the purkinje cell by loading it from specificaiton ?",
						   read => {
							    application_output_file => "/tmp/output",
							    expected_output_file => "$::config->{core_directory}/tests/specifications/strings/edsjb1994-perfectclamp.txt",
							   },
						  },
						 ],
				description => "Test the purkinje cell with perfectclamp from specification",
				timeout => 300,
				disabled => "Can't get outputs to match",
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
				command => 'tests/python/edsjb1994-perfectclamp_api.py',
				disabled => "Can't get outputs to match",
				command_tests => [
						  {
						   description => "Check for script completion",
						   read => 'Done!',
						   timeout => 300,
						  },
						  {
						   description => "Can we clamp the purkinje cell by loading it via API ?",
						   read => {
							    application_output_file => "/tmp/output",
							    expected_output_file => "$::config->{core_directory}/tests/specifications/strings/edsjb1994-perfectclamp.txt",
							   },
						  },
						 ],
				description => "Test the purkinje cell with perfectclamp from api",
				timeout => 200,
				disabled => "Can't get outputs to match",
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
       description => "Perfectclamp module tests",
       name => 'perfectclamp.t',
      };


return $test;


