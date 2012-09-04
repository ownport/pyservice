import sys
import unittest

from cStringIO import StringIO
from pyservice import ServiceControl

class ServiceControlTests(unittest.TestCase):
    
    def test_service_control_start(self):
        self.assertEqual(ServiceControl('tests.processes.simple_process.SimpleProcess').start(), None)

    
if __name__ == '__main__':
    unittest.main()        
    
