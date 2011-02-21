#!/usr/bin/perl -w
#

use strict;


my $test
    = {
       command_definitions => [

			       {
				arguments => [
					     ],
				command => 'tests/python/service_1.py',
				command_tests => [
						  {

						   disabled => "Disabled while fixing some issues",
						   description => "Can we load a service specification from a YAML file ?",

						   read => "Parsing schedule data
Loading Service 'Untitled (test)' of type 'test'
Loading Service 'Untitled (test 2)' of type 'test 2'
This service name is 'Untitled (test)'
This service name is 'Untitled (test 2)'
",

						  },
						 ],
				description => "Simple load and dump of a specification with service data.",
			       },
			       {
				arguments => [
					     ],
				command => 'tests/python/service_2.py',
				command_tests => [
						  {

						   description => "Can we load a service specification from a YAML file ?",

						   read => "Parsing schedule data
Loading Service 'Untitled (heccer_intermediary)' of type 'heccer_intermediary'
Loading Solver 'Untitled (heccer)' of type 'heccer'
This service name is 'Untitled (heccer_intermediary)'
",

						  },
						 ],
				description => "Simple load and dump of a specification with a heccer intermediary service.",
			       },

			      ],
       description => "Tests generated service objects.",
       name => 'services.t',
      };


return $test;


