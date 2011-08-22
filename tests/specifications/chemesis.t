#!/usr/bin/perl -w
#

use strict;


# slurp mode

local $/;


my $test
    = {
       command_definitions => [
			       {
				arguments => ['./yaml/cal1.yml'
					     ],
				command => './sspy',
				command_tests => [

						  {
						   description => "Can we find the expected output for cal1.py via declaration ?",
						   wait => 4,
						   read => {
							    application_output_file => "/tmp/output_cal1_ssp",
							    expected_output_file => "$::config->{core_directory}/tests/specifications/strings/cal1.txt",
							   },
						  },
						 ],
				description => "Schedule based on the G-2 cal1.g script",
				preparation => {
						description => "Clean out any previous files",
						preparer =>
						sub
						{
						    `rm -f /tmp/output_cal1_ssp`;
						},
					       },
				reparation => {
					       description => "Remove the generated output files",
					       reparer =>
					       sub
					       {
 						   `rm -f /tmp/output_cal1_ssp`;
					       },
					      },

			       },

			      ],
       description => "",
       name => 'chemesis.t',
      };


return $test;


