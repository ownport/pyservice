import sys
import unittest

from pyservice import runner
from cStringIO import StringIO

#sys.stdout = my_stdout = StringIO()
#sys.stderr = my_stderr = StringIO()
#sys.exit = lambda x: x

# TODO make runner tests more actual

class RunnerTests(unittest.TestCase):
        
    def test_runner_show_help(self):
        sys.argv = list()    
        sys.argv.append('pyservice')
        sys.argv.append('-h')
        runner.run_service()

    def test_runner_by_process_name(self):
        sys.argv = list()    
        sys.argv.append('pyservice')
        sys.argv.append('dummy_process')
        sys.argv.append('start')
        runner.run_service()

    def test_runner_by_process_name_no_action(self):
        sys.argv = list()    
        sys.argv.append('pyservice')
        sys.argv.append('dummy_process')
        runner.run_service()

class ServiceControlTests(unittest.TestCase):
    
    def test_service_control_start(self):
        self.assertEqual(runner.ServiceControl('tests.processes.simple_process.SimpleProcess').start(), None)

    


if __name__ == '__main__':
    unittest.main()        
    
