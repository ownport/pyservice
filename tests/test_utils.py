import os
import unittest

from pyservice import Pidfile
from pyservice import load_process


class UtilsTests(unittest.TestCase):
        
    def test_pidfile(self):
        
        pid = Pidfile('tests/run/test1.pid')
        pid.create()
        self.assertEqual(pid.validate(), os.getpid())
        pid.unlink()
        self.assertEqual(pid.validate(), None)

    def test_load_process(self):
        self.assertRaises(RuntimeError, load_process, 'simple_process')
        self.assertRaises(RuntimeError, load_process, 'examples.simple_process')
        
        self.assertEqual(
            load_process('tests.processes.simple_process.SimpleProcess').__name__, 
            'SimpleProcess')
        self.assertEqual(
            load_process('tests.processes.few_simple_process.SimpleProcess1').__name__, 
            'SimpleProcess1')
        self.assertEqual(
            load_process('tests.processes.few_simple_process.SimpleProcess2').__name__, 
            'SimpleProcess2')
        

if __name__ == '__main__':
    unittest.main()        

