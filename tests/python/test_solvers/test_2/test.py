



class Solver:

#---------------------------------------------------------------------------

    def __init__(self, name=None, constructor_settings=None, verbose=False):
        """

        Should be able to pass the scheudler and use it as
        an internal member here.
        """
        self._name = name

        self._scheduler = None

        self._value = -1.0

#---------------------------------------------------------------------------

    def SetConfiguration(self, config):

        pass
    
#---------------------------------------------------------------------------

    def New(self, modelname="test 2", filename="file: test 2"):

        print "Modelname %s, Filename %s" % (modelname, filename)
        

#---------------------------------------------------------------------------

    def Advance(self):

        print "Test 2 Advance"

#---------------------------------------------------------------------------

    def Compile(self):

        print "Test 2 Compile"

#---------------------------------------------------------------------------

    def Connect(self):

        print "Test 2 Connect"

#---------------------------------------------------------------------------

    def Deserialize(self, filename="file: test 2"):

        print "Test 2 Deserialize"

#---------------------------------------------------------------------------

    def DeserializeState(self, filename="file: test 2"):

        print "Test 2 Deserilize State"

#---------------------------------------------------------------------------

    def Finish(self):

        print "Test 2 Finish"

#---------------------------------------------------------------------------

    def Name(self):

        print "Test 2 Name: %s" % self._name

        return self._name

#---------------------------------------------------------------------------

    def SetSolverField(self, field="Vm", value=1.0):

        print "Test 2 SetSolverField, Field: %s, Value: %f" % (field, value)

#---------------------------------------------------------------------------

    def GetSolverField(self, field="Vm"):

        print "Test 2 GetSolverField, Field: %s, Value: %f" % (field, self._value)

#---------------------------------------------------------------------------


    def Serialize(self, filename="file: test 2"):

        print "Test 2 Serialize, Filename: %s" % filename

#---------------------------------------------------------------------------

    def SerializeState(self, filename="file: test 2"):

        print "Test 2 SeriaizeState, Filename: %s" % filename

#---------------------------------------------------------------------------
        
    def Output(self, serial=1, field="Vm"):

        print "Test 2 Serial and field is %d:%s" % (serial, field)

#---------------------------------------------------------------------------

    def Run(self, time=100):

        print "Test 2 Simulation time is %s" % time

#---------------------------------------------------------------------------

    def Step(self):

        print "Test 2 Step"

#---------------------------------------------------------------------------

    def Steps(self, steps=100):

        print "Test 2 Steps %d" % steps



  
