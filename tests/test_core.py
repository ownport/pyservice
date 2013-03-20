import os
import time
import pyservice

def test_service_start():
    process = pyservice.load_process('tests.processes.simple_process.SimpleProcess')
    service = pyservice.Service(process)
    service.start()
    print process, service

def test_service_stop():
    time.sleep(1)
    process = pyservice.load_process('tests.processes.simple_process.SimpleProcess')
    service = pyservice.Service(process)
    service.stop()
    print process, service
                        
