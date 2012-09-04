import os
import unittest
import pyservice

class Process1Tests(unittest.TestCase):
        
    def test_run_process1(self):
        process1 = pyservice.load_process('tests.processes.few_simple_process.SimpleProcess1')
        service1 = pyservice.Service(process1)
        service1.start()
                    
        
if __name__ == '__main__':
    unittest.main(exit=False)        

