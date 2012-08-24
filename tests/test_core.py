import os
import time
import unittest
import pyservice

class CoreTests(unittest.TestCase):
        
    def test_service_start(self):
        process = pyservice.utils.load_process('tests.processes.simple_process.SimpleProcess')
        service = pyservice.Service(process)
        service.start()

    def test_service_stop(self):
        time.sleep(1)
        process = pyservice.utils.load_process('tests.processes.simple_process.SimpleProcess')
        service = pyservice.Service(process)
        service.stop()
                        
        
if __name__ == '__main__':
    unittest.main(exit=False)        

