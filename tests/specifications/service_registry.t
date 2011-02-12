#!/usr/bin/perl -w
#

use strict;


my $test
    = {
       command_definitions => [

			       {
				arguments => [
					     ],
				command => 'tests/python/service_registry_1.py',
				command_tests => [
						  {
						   disabled => "Disabled for now due to an order problem",
						   description => "Can we load some service plugins from a plugin directory ?",

						   read => "List of plugins:
['tests/python/test_services/test/service.yml', 'tests/python/test_services/test_2/service.yml']

List of loaded service plugins:
  Plugin name: test
  Plugin name: test 2
Done
",

						  },
						 ],
				description => "Checks the service plugin directory for available services.",
			       },

			      ],
       description => "Tests the registry module for dynamically creating modeling service objects",
       name => 'service_registry.t',
      };


return $test;


