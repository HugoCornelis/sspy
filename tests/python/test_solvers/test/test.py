



class Solver:

#---------------------------------------------------------------------------

    def __init__(self, name):
        """

        Should be able to pass the scheudler and use it as
        an internal member here.
        """
        self._name = name

        self._scheduler = None

        self._value = -1.0

#---------------------------------------------------------------------------

    def New(self, modelname="test 1", filename="file: test 1"):

        print "Modelname %s, Filename %s" % (modelname, filename)
        

#---------------------------------------------------------------------------

    def Advance(self):

        print "Test 1 Advance"

#---------------------------------------------------------------------------

    def Compile(self):

        print "Test 1 Compile"

#---------------------------------------------------------------------------

    def Connect(self):

        print "Test 1 Connect"

#---------------------------------------------------------------------------

    def Deserialize(self, filename="file: test 1"):

        print "Test 1 Deserialize"

#---------------------------------------------------------------------------

    def DeserializeState(self, filename="file: test 1"):

        print "Test 1 Deserilize State"

#---------------------------------------------------------------------------

    def Finish(self):

        print "Test 1 Finish"

#---------------------------------------------------------------------------

    def Name(self):

        print "Test 1 Name: %s" % self._name

        return self._name

#---------------------------------------------------------------------------

    def SetSolverField(self, field="Vm", value=1.0):

        print "Test 1 SetSolverField, Field: %s, Value: %f" % (field, value)

#---------------------------------------------------------------------------

    def GetSolverField(self, field="Vm"):

        print "Test 1 GetSolverField, Field: %s, Value: %f" % (field, self._value)

#---------------------------------------------------------------------------


    def Serialize(self, filename="file: test 1"):

        print "Test 1 Serialize, Filename: %s" % filename

#---------------------------------------------------------------------------

    def SerializeState(self, filename="file: test 1"):

        print "Test 1 SeriaizeState, Filename: %s" % filename

#---------------------------------------------------------------------------
        
    def Output(self, serial=1, field="Vm"):

        print "Test 1 Serial and field is %d:%s" % (serial, field)

#---------------------------------------------------------------------------

    def Run(self, time=100):

        print "Test 1 Simulation time is %s" % time

#---------------------------------------------------------------------------

    def Step(self):

        print "Test 1 Step"

#---------------------------------------------------------------------------

    def Steps(self, steps=100):

        print "Test 1 Steps %d" % steps



  
