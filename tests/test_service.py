from pyservice import Process
from pyservice import service

class TestProcess(Process):
    ''' TestProcess
    '''
    pidfile = 'run/test_service.test_process.pid'
    logfile = 'logs/test_service.test_process.pid'
    
    def run(self):
        self.logger.info('TestProcess.run() started')
        self.logger.info('TestProcess.run() stopped')


def test_service_create():
    ''' test_servce.test_service_create
    '''
    
    test_service = service('tests.test_service.TestProcess', 'start')
    
