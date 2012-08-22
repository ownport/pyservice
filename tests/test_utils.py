import unittest

from pyservice.utils import resolve_pid

class UtilsTests(unittest.TestCase):
        
    def test_resolve_pid(self):
        self.assertRaises(RuntimeError, resolve_pid, (None, None))


if __name__ == '__main__':
    unittest.main()        

