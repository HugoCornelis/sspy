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
				command => 'tests/python/springmass3.py',
				command_tests => [
						  {
						   description => "Check for script completion",
						   read => 'Done!',
						   timeout => 10,
						  },
						  {
						   description => "Is a synaptic (springmass) channel with an event table integrated correctly ?",
						   read => {
							    application_output_file => "/tmp/output",
							    expected_output_file => "$::config->{core_directory}/tests/specifications/strings/springmass3.txt",
							   },
						  },
						 ],
				description => "synaptic (springmass) channel integration, with an event table",
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
				command => 'tests/python/springmass4.py',
				command_tests => [
						  {
						   description => "Check for script completion",
						   read => 'Done!',
						  },
						  {
						   description => "Is a synaptic (springmass) channel with an event table integrated correctly ?",
						   read => {
							    application_output_file => "/tmp/output",
							    expected_output_file => "$::config->{core_directory}/tests/specifications/strings/springmass4.txt",
							   },
						  },
						 ],
				description => "synaptic (springmass) channel integration, with an event table",
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
       description => "synaptic channels",
       name => 'synaptic.t',
      };


return $test;


