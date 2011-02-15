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

			      ],
       disabled => "Disabled while fixing some issues",
       description => "Tests generated service objects.",
       name => 'services.t',
      };


return $test;


