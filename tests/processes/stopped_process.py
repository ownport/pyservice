import os
import time
import pyservice

class StoppedProcess(pyservice.Process):
    
    pidfile = os.path.join(os.getcwd(), 'tests/run/simple_process.pid')
    logfile = os.path.join(os.getcwd(), 'tests/log/simple_process.log')
    
    def do_stop(self):
        print 'The process is stopping'
    
    def run(self):
        time.sleep(10)

