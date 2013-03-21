import os
import time
import pyservice

def test_service_start():
    process = pyservice.load_process('tests.processes.simple_process.SimpleProcess')
    service = pyservice.Service(process)
    service.start()
    assert process <> None, process
    assert service <> None, service

def test_service_stop():
    time.sleep(2)
    process = pyservice.load_process('tests.processes.simple_process.SimpleProcess')
    service = pyservice.Service(process)
    service.stop()
    assert process <> None, process
    assert service <> None, service

