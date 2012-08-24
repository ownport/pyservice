import sys
import unittest

from pyservice import runner
from cStringIO import StringIO

class ServiceControlTests(unittest.TestCase):
    
    def test_service_control_start(self):
        self.assertEqual(runner.ServiceControl('tests.processes.simple_process.SimpleProcess').start(), None)

    
if __name__ == '__main__':
    unittest.main()        
    
