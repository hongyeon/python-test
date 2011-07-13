import unittest


class Tuple():
    
    temp = 0
    huminity = 0
    def __init__(self, temp, huminity):
        self.temp  = temp
        self.huminity = huminity
    

# if return value is -1, this tuple1 was dominated by  tuple2.
# if return value is 0, any tuple can not dominate another tuple, 
# if return value is 1, tuple1 dominates tuple2.
def compare(tuple1, tuple2):
    if (tuple1.temp < tuple2.temp and tuple1.huminity < tuple2.huminity) :
        return 1
    elif(tuple2.temp < tuple1.temp and tuple2.huminity < tuple1.huminity):
        return -1
    else:
        return 0
    
class Window():
    
    
    def __init__(self):
        self.tuples = list()
    
    def handle(self, tuple):
        self.tuples.append(tuple)
        
    def size(self):
        return self.tuples.__len__()
        
        
    
    
class WindowTest(unittest.TestCase):
    def test_handle(self) :
        window  = Window()
        
        tuple = Tuple(10,10)
        window.handle(tuple)
        
        self.assertEquals(window.size(),1)
    
    

#
#    
#    
#    
#class BNLTest(unittest.TestCase):
#    def setUp(self):
#        self.inputs = list()        
#        self.inputs.append(Tuple(10, 10))
#        self.inputs.append(Tuple(20, 20))
#        self.inputs.append(Tuple(10, 20))
#        
#        self.window = Window()
#        
#        for i in self.inputs:
#            
#        
#    def sdafadfasdf(self):
#        self.inputs.pop()
#        for 
#        
#        
        
        
        
    

class SimpleTest(unittest.TestCase):    
    def setUp(self):
        self.inputs = list()
        self.tuple1 = Tuple(10, 10)
        self.tuple2 = Tuple(20, 20)
        self.tuple3 = Tuple(10, 20)
        

    def test_compare(self):
        self.assertTrue(compare(self.tuple1, self.tuple2) ==1)
        self.assertTrue(compare(self.tuple2, self.tuple1) == -1)
        self.assertTrue(compare(self.tuple2, self.tuple3) ==0)
        self.assertTrue(compare(self.tuple1, self.tuple3) ==0)


suite = unittest.TestLoader().loadTestsFromTestCase(SimpleTest)
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(WindowTest))
unittest.TextTestRunner(verbosity=2).run(suite)

       
    
