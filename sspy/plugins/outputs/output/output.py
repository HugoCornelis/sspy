


class Output:

    def __init__(self):

        self._output_gen = None

    
        self._output_var = "output"

    def Connect(self, solver):


        solver_type = solver.GetType()

        if solver_type == 'heccer':

            #
            # Here we use modelname to get the 
            # membrane potential. 
            address = solver.GetAddress(modelname, "Vm")

            self._output_gen.AddOutput(self._output_var, address) 


    def Step(self):
        """

        """
        self._output_gen.Step()


    def 
