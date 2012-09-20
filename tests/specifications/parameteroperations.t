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
				command => 'tests/python/parameter_operation_1.py',
				command_tests => [
						  {
						   description => "Can we retrieve the INJECT parameter from the scheduler ?",
						   read => 'INJECT value before run prepare is: 2e-09
INJECT value after run prepare is: 2e-09
Done!
',


						  },
						 ],
				description => "Returns the INJECT value that is set via script",
				timeout => 15,
			       },
			      ],
       description => "Some test for setting and retrieving parameters",
       name => 'parameteroperations.t',
      };


return $test;


