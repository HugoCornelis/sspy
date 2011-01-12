#!/usr/bin/perl -w
#

use strict;


my $test
    = {
       command_definitions => [
			       {
				arguments => [
					     ],
				command => 'tests/python/getversion.py',
				command_tests => [
						  {
						   # $Format: "description => \"Does the version information match with ${package}-${label} ?\","$
description => "Does the version information match with sspy-alpha ?",

						   # $Format: "read => \"${package}-${label}\","$
read => "sspy-alpha",

						   write => "version",
						  },
						 ],
				description => "check version information in python",
			       },
			      ],
       description => "run-time versioning",
       name => 'version.t',
      };


return $test;


