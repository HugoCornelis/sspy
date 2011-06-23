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
					      '--shell'
					     ],
				command => './sspy',
				disabled => 'working on this',
				timeout => 50,
				command_tests => [
						  {
						   description => "Load the purk_test ndf file via shell",
						   write => 'ndf_load tests/cells/purk_test.ndf',
						   wait => 1,
						  },

						  {
						   description => "Set a model parameter for injection",
						   write => 'model_parameter_add /purk_test/segments/soma INJECT 2e-09',
						   wait => 1,

						  },

						  {
						   description => "Set the time step",
						   write => 'heccer_set_timestep 2e-05',
						   wait => 1,

						  },

						  {
						   description => "Adding output 1",
						   write => 'output_add /purk_test/segments/soma Vm',
						   wait => 1,

						  },

						  {
						   description => "Adding output 2",
						   write => 'output_add /purk_test/segments/soma/ca_pool Ca',
						   wait => 1,

						  },

						  {
						   description => "Adding output 3",
						   write => 'output_add /purk_test/segments/soma/km state_n',
						   wait => 1,

						  },

						  {
						   description => "Adding output 4",
						   write => 'output_add /purk_test/segments/soma/kdr state_m',
						   wait => 1,

						  },

						  {
						   description => "Adding output 5",
						   write => 'output_add /purk_test/segments/soma/kdr state_h',
						   wait => 1,

						  },


						  {
						   description => "Adding output 6",
						   write => 'output_add /purk_test/segments/soma/ka state_m',
						   wait => 1,

						  },

						  {
						   description => "Adding output 7",
						   write => 'output_add /purk_test/segments/soma/ka state_h',
						   wait => 1,

						  },

						  {
						   description => "Adding output 8",
						   write => 'output_add /purk_test/segments/soma/kh state_m',
						   wait => 1,

						  },

						  {
						   description => "Adding output 9",
						   write => 'output_add /purk_test/segments/soma/kh state_h',
						   wait => 1,

						  },
						  {
						   description => "Adding output 10",
						   write => 'output_add /purk_test/segments/soma/nap state_n',
						   wait => 1,

						  },

						  {
						   description => "Adding output 11",
						   write => 'output_add /purk_test/segments/soma/naf state_m',
						   wait => 1,

						  },

						  {
						   description => "Adding output 12",
						   write => 'output_add /purk_test/segments/soma/naf state_h',
						   wait => 1,

						  },
						  {
						   description => "Adding output 13",
						   write => 'output_add /purk_test/segments/soma/cat/cat_gate_activation state_m',
						   wait => 1,

						  },

						  {
						   description => "Adding output 14",
						   write => 'output_add /purk_test/segments/soma/cat/cat_gate_activation state_h',
						   wait => 1,

						  },


						  {
						   description => "Adding output 15",
						   write => 'output_add /purk_test/segments/main[0] Vm',
						   wait => 1,

						  },


						  {
						   description => "Adding output 16",
						   write => 'output_add /purk_test/segments/main[0]/ca_pool Ca',
						   wait => 1,

						  },



						  {
						   description => "Adding output 17",
						   write => 'output_add /purk_test/segments/main[0]/cat/cat_gate_activation state_m',
						   wait => 1,

						  },

						  {
						   description => "Adding output 18",
						   write => 'output_add /purk_test/segments/main[0]/cat/cat_gate_inactivation state_h',
						   wait => 1,

						  },
						  {
						   description => "Adding output 19",
						   write => 'output_add /purk_test/segments/main[0]/cap/cap_gate_activation state_m',
						   wait => 1,

						  },

						  {
						   description => "Adding output 20",
						   write => 'output_add /purk_test/segments/main[0]/cap/cap_gate_inactivation state_h',
						   wait => 1,

						  },


						  {
						   description => "Adding output 21",
						   write => 'output_add /purk_test/segments/main[0]/km state_n',
						   wait => 1,

						  },

						  {
						   description => "Adding output 22",
						   write => 'output_add /purk_test/segments/main[0]/kdr state_m',
						   wait => 1,

						  },


						  {
						   description => "Adding output 23",
						   write => 'output_add /purk_test/segments/main[0]/kdr state_h',
						   wait => 1,

						  },


						  {
						   description => "Adding output 24",
						   write => 'output_add /purk_test/segments/main[0]/ka state_m',
						   wait => 1,

						  },


						  {
						   description => "Adding output 25",
						   write => 'output_add /purk_test/segments/main[0]/ka state_h',
						   wait => 1,

						  },


						  {
						   description => "Adding output 26",
						   write => 'output_add /purk_test/segments/main[0]/kc state_m',
						   wait => 1,

						  },


						  {
						   description => "Adding output 27",
						   write => 'output_add /purk_test/segments/main[0]/kc state_h',
						   wait => 1,

						  },


						  {
						   description => "Adding output 28",
						   write => 'output_add /purk_test/segments/main[0]/k2 state_m',
						   wait => 1,

						  },


						  {
						   description => "Adding output 29",
						   write => 'output_add /purk_test/segments/main[0]/k2 state_h',
						   wait => 1,

						  },


						  {
						   description => "Run the simulation",
						   write => 'run /purk_test 2500',
						   wait => 30,
						  },


						 ],

			       },

			      ],
       description => "Purk test run from the shell",
       name => 'purk_test_shell.t',
      };


return $test;


