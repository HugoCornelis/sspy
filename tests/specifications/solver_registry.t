#!/usr/bin/perl -w
#

use strict;


my $test
    = {
       command_definitions => [
			       {
				arguments => [
					     ],
				command => 'tests/python/solver_registry_2.py',
				command_tests => [
						  {
						   description => "Can we create seperate dynamically allocated solver objects ?",

						   read => "Printing output of solver 1
Modelname test 1, Filename file: test 1
Test 1 Advance
Test 1 Compile
Test 1 Connect
Test 1 Deserialize
Test 1 Deserilize State
Test 1 Finish
Test 1 Name: my solver 1
Test 1 SetSolverField, Field: Vm, Value: 1.000000
Test 1 GetSolverField, Field: Vm, Value: -1.000000
Test 1 Serialize, Filename: file: test 1
Test 1 SeriaizeState, Filename: file: test 1
Test 1 Serial and field is 1:Vm
Test 1 Simulation time is 100
Test 1 Step
Test 1 Steps 100


Printing output of solver 2
Modelname test 2, Filename file: test 2
Test 2 Advance
Test 2 Compile
Test 2 Connect
Test 2 Deserialize
Test 2 Deserilize State
Test 2 Finish
Test 2 Name: my solver 2
Test 2 SetSolverField, Field: Vm, Value: 1.000000
Test 2 GetSolverField, Field: Vm, Value: -1.000000
Test 2 Serialize, Filename: file: test 2
Test 2 SeriaizeState, Filename: file: test 2
Test 2 Serial and field is 1:Vm
Test 2 Simulation time is 100
Test 2 Step
Test 2 Steps 100
Done
",

						  },
						 ],
				description => "Dynamically allocate a solver via a registry.",
			       },
			      ],
       description => "Tests the registry module for dynamically creating solvers or sim objects",
       name => 'solver_registry.t',
      };


return $test;


