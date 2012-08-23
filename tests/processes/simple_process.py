import os
import time
import pyservice

class SimpleProcess(pyservice.Process):
    
    pidfile = os.path.join(os.getcwd(), 'tests/run/simple_process.pid')
    logfile = os.path.join(os.getcwd(), 'tests/log/simple_process.log')
    
    def run(self):
        time.sleep(10)
