import os
import time
import pyservice

class SimpleProcess(pyservice.Process):
    
    pidfile = os.path.join(os.getcwd(), 'run/simple_process.pid')
    logfile = os.path.join(os.getcwd(), 'logs/simple_process.log')
    
    def run(self):
        self.logger.info('Process.run() started')
        time.sleep(10)
        self.logger.info('Process.run() stopped')

