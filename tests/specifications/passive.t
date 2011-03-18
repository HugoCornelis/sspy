#!/usr/bin/perl -w
#

use strict;


my $test
    = {
       command_definitions => [

			       {
				arguments => [
					     ],
				command => 'tests/python/singlep.py',
				command_tests => [
						  {
						   description => "Is a single passive compartment solved correctly ?",
						   read => (join '', `cat tests/specifications/strings/singlep.txt`),
						   timeout => 15,

						  },
						 ],
				description => "single passive compartment",
			       },


			       {
				arguments => [
					     ],
				command => 'tests/python/singlea-naf.py',
				command_tests => [
						  {
						   description => "Is a single compartment with active channels solved correctly in passive mode ?",
						   read => (join '', `cat tests/specifications/strings/singlea-naf.txt`),
						   timeout => 15,

						  },
						 ],
				description => "single active compartment in passive mode",
			       },

			      ],
       description => "simple passive model testing",
       name => 'passive.t',
      };


return $test;


