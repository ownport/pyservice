import os
import time
import pyservice

class SimpleProcess1(pyservice.Process):

    pidfile = os.path.join(os.getcwd(), 'run/simple_process1.pid')
    logfile = os.path.join(os.getcwd(), 'logs/simple_process.log')
    
    def run(self):
        time.sleep(10)
            
class SimpleProcess2(pyservice.Process):

    pidfile = os.path.join(os.getcwd(), 'run/simple_process2.pid')
    logfile = os.path.join(os.getcwd(), 'logs/simple_process.log')
    
    def run(self):
        time.sleep(10)

