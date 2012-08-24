import os
import unittest
import pyservice

class CoreTests(unittest.TestCase):
        
    def test_service_start(self):
        process = pyservice.utils.load_process('tests.processes.simple_process.SimpleProcess')
        service = pyservice.Service(process)
        service.start()

    def test_run_multiple_processes(self):
        process1 = pyservice.utils.load_process('tests.processes.few_simple_process.SimpleProcess1')
        service1 = pyservice.Service(process1)
        service1.start()
        process2 = pyservice.utils.load_process('tests.processes.few_simple_process.SimpleProcess2')
        service2 = pyservice.Service(process2)
        service2.start()
                    
        
if __name__ == '__main__':
    unittest.main(exit=False)        

