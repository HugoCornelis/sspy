ndf_load tests/cells/purk_test.ndf
model_parameter_add /purk_test/segments/soma INJECT 2e-09
heccer_set_timestep 2e-05
output_add /purk_test/segments/soma Vm
output_add /purk_test/segments/soma/ca_pool Ca
output_add /purk_test/segments/soma/km state_n
output_add /purk_test/segments/soma/kdr state_m
output_add /purk_test/segments/soma/kdr state_h
output_add /purk_test/segments/soma/ka state_m
output_add /purk_test/segments/soma/ka state_h
output_add /purk_test/segments/soma/kh state_m
output_add /purk_test/segments/soma/kh state_h
output_add /purk_test/segments/soma/nap state_n
output_add /purk_test/segments/soma/naf state_m
output_add /purk_test/segments/soma/naf state_h
output_add /purk_test/segments/soma/cat/cat_gate_activation state_m
output_add /purk_test/segments/soma/cat/cat_gate_activation state_h
output_add /purk_test/segments/main[0] Vm
output_add /purk_test/segments/main[0]/ca_pool Ca
output_add /purk_test/segments/main[0]/cat/cat_gate_activation state_m
output_add /purk_test/segments/main[0]/cat/cat_gate_inactivation state_h
output_add /purk_test/segments/main[0]/cap/cap_gate_activation state_m
output_add /purk_test/segments/main[0]/cap/cap_gate_inactivation state_h
output_add /purk_test/segments/main[0]/km state_n
output_add /purk_test/segments/main[0]/kdr state_m
output_add /purk_test/segments/main[0]/kdr state_h
output_add /purk_test/segments/main[0]/ka state_m
output_add /purk_test/segments/main[0]/ka state_h
output_add /purk_test/segments/main[0]/kc state_m
output_add /purk_test/segments/main[0]/kc state_h
output_add /purk_test/segments/main[0]/k2 state_m
output_add /purk_test/segments/main[0]/k2 state_h
run /purk_test 2500
