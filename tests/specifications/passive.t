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

			      ],
       description => "Tests generated solver objects.",
       name => 'passive.t',
      };


return $test;


