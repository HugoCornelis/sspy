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
Found services:
	{'test': {'module_name': 'Neurospaces', 'initializers': [{'arguments': [['tests/perl/purk_test', '-P', 'tests/cells/purk_test.ndf']], 'method': 'read'}]}, 'test 2': {'module_name': 'Neurospaces', 'initializers': [{'arguments': [['tests/perl/purk_test', '-P', 'tests/cells/purk_test.ndf']], 'method': 'read'}]}}

Loading service 'Untitled (test)' of type 'test'
Loading service 'Untitled (test 2)' of type 'test 2'
This service name is 'Untitled (test 2)'
This service name is 'Untitled (test)'
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

						   read => "Loading service 'Untitled (heccer_intermediary)' of type 'heccer_intermediary'
Found Solver Classes:
	{'heccer': {'constructor_settings': {'configuration': {'reporting': {'tested_things': 6225920, 'granularity': 100}}, 'dStep': '1e-06'}, 'module_name': 'Heccer', 'service_name': 'heccer_intermediary'}}

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


