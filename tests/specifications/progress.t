#!/usr/bin/perl -w
#

use strict;


my $test
    = {
       command_definitions => [

			       {
				arguments => [
					     ],
				command => 'tests/python/progress_1.py',
				command_tests => [
						  {
						   description => "Can we check the progress on a simulation in steps mode ?",
						   read => "Finishing simulation
Simulation is 1.000000 % complete
",
						   timeout => 15,

						  },
						 ],
				description => "Can we check progress in steps mode",
			       },


			       {
				arguments => [
					     ],
				command => 'tests/python/progress_2.py',
				command_tests => [
						  {
						   description => "Can we check the progress on a simulation in time mode ?",
						   read => "Finishing simulation
Simulation is 1.000000 % complete
",
						   timeout => 15,

						  },
						 ],
				description => "Can we check progress in time mode",
			       },


			      ],
       description => "Test the progress check",
       name => 'progress.t',
      };


return $test;


