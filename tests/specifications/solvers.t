#!/usr/bin/perl -w
#

use strict;


my $test
    = {
       command_definitions => [

			       {
				arguments => [
					     ],
				command => 'tests/python/solver_1.py',
				command_tests => [
						  {
						   description => "Can we load a solver specification from a YAML file ?",

						   read => "Parsing schedule data
Schdule name is 'solver test'

Found Solver Classes:
	{'test': {'constructor_settings': {'configuration': {'reporting': {'tested_things': 6225920, 'granularity': 100000}}, 'options': {'iOptions': 4}, 'dStep': '1e-05'}, 'module_name': 'Heccer', 'service_name': 'model_container'}}

Loading Solver 'solver test (test)' of type 'test'
Dumping schedule data for tests/yaml/solver_1.yml

name: solver test
solverclasses:
  test:
    constructor_settings:
      configuration:
        reporting: {granularity: 100000, tested_things: 6225920}
      dStep: 1e-05
      options: {iOptions: 4}
    module_name: Heccer
    service_name: model_container
",

						  },
						 ],
				description => "Simple load and dump of a specification with solver data.",
			       },

			      ],
       description => "Tests generated solver objects.",
       name => 'solver.t',
      };


return $test;


