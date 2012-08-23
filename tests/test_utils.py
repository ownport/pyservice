import os
import unittest

from pyservice.utils import Pidfile

class UtilsTests(unittest.TestCase):
        
    def test_pidfile(self):
        pid = Pidfile('tests/run/test1.pid')
        pid.create()
        self.assertEqual(pid.validate(), os.getpid())
        pid.unlink()
        self.assertEqual(pid.validate(), None)
        

if __name__ == '__main__':
    unittest.main()        

