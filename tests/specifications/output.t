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
						   description => "Can we produce simple output with simulation time?",
						   read => {
							    application_output_file => "/tmp/output",
							    expected_output_file => "$::config->{core_directory}/tests/specifications/strings/output1.txt",
							   },
						  },
						 ],
				description => "simple output with simulation time",


			       },

			       {
				arguments => [
					     ],
				command => 'tests/python/output2.py',
				command_tests => [
						  {
						   description => "Can we produce simple output with the steps mode?",
						   read => {
							    application_output_file => "/tmp/output",
							    expected_output_file => "$::config->{core_directory}/tests/specifications/strings/output2.txt",
							   },
						  },
						 ],
				description => "simple output with the steps mode",


			       },
			       {
				arguments => [
					     ],
				command => 'tests/python/output3.py',
				command_tests => [
						  {
						   description => "Can we produce output with the steps mode at a coarser resolution?",
						   read => {
							    application_output_file => "/tmp/output",
							    expected_output_file => "$::config->{core_directory}/tests/specifications/strings/output1.txt",
							   },

						  },
						 ],
				description => "output with the steps mode at a coarser resolution",


			       },
			       {
				arguments => [
					     ],
				command => 'tests/python/output4.py',
				command_tests => [
						  {
						   description => "Can we produce simple output with the steps mode and a format field?",
						   read => {
							    application_output_file => "/tmp/output",
							    expected_output_file => "$::config->{core_directory}/tests/specifications/strings/output1.txt",
							   },

						  },
						 ],
				description => "simple output with the steps mode and a format field",


			       },
			      ],
       description => "output functions",
       name => 'output.t',
      };


return $test;


