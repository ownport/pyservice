import os

from pyservice import Pidfile
from pyservice import file_logger
from pyservice import load_process


def test_file_logger():
        
    logger = file_logger('test_file_logger', 'logs/test_file_logger.log')
    logger.info('test_file_logger message')
        
def test_pidfile():
        
    pid = Pidfile('tests/run/test1.pid')
    pid.create()
    assert pid.validate() == os.getpid()
    pid.unlink()
    assert pid.validate() == None

def test_load_process():
    
    try:    
        process = load_process('simple_process')
    except RuntimeError:
        pass
    
    try:    
        process = load_process('examples.simple_process')
    except RuntimeError:
        pass
    
    assert load_process('tests.processes.simple_process.SimpleProcess').__name__ == 'SimpleProcess'
    assert load_process('tests.processes.few_simple_process.SimpleProcess1').__name__ == 'SimpleProcess1'
    assert load_process('tests.processes.few_simple_process.SimpleProcess2').__name__ == 'SimpleProcess2'
        

