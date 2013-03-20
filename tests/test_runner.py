from pyservice import ServiceControl

def test_service_control_start(self):
    ''' test_runner.service_control_start
    '''
    assert ServiceControl('tests.processes.simple_process.SimpleProcess').start() == None

    
