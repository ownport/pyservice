import os
import unittest
import pyservice

class Process2Tests(unittest.TestCase):
        
    def test_run_process1(self):
        process2 = pyservice.utils.load_process('tests.processes.few_simple_process.SimpleProcess2')
        service2 = pyservice.Service(process2)
        service2.start()
                    
        
if __name__ == '__main__':
    unittest.main(exit=False)        

