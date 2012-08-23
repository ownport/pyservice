''' core '''

import os
import sys
import time
import signal
import atexit
import logging

from .utils import Pidfile
from .utils import set_logging

SIGNAL_STOP = signal.SIGTERM
SIGNAL_RELOAD = signal.SIGHUP

sys.path.insert(0, os.getcwd())

# -----------------------------------------------------
#   classes
# -----------------------------------------------------
class Process(object):
    
    pidfile = None  # Override this field for your class
    logfile = None  # Override this field for your class
    
    def run(self):
        """
        You should override this method when you subclass Process. It will be called after the process has been
        daemonized by start() or restart() via Service class.
        """
        pass

class Service(object):
    """ Service class  """
    
    def __init__(self, process):
        ''' init '''
        
        self.process = process
        self.pidfile = Pidfile(process.pidfile)
        if process.logfile:
            set_logging(process.logfile)            
    
    def _fork(self, fid):
        ''' fid - fork id'''
        
        try: 
            pid = os.fork() 
            if pid > 0:
                # exit from parent
                return 
        except OSError, e: 
            # sys.stderr.write("fork #1 failed: %d (%s)\n" % (e.errno, e.strerror))
            logging.error("service.daemonize(), fork #%d failed: %d (%s)\n" % (fid, e.errno, e.strerror))
            raise OSError(e)       
    
    def daemonize(self):
        """
        do the UNIX double-fork magic, see Stevens' "Advanced 
        Programming in the UNIX Environment" for details (ISBN 0201563177)
        http://www.erlenstar.demon.co.uk/unix/faq_2.html#SEC16
        """
        # TODO check why processes are running twice
        
        self._fork(1) # first fork
    
        # decouple from parent environment
        os.chdir("/") 
        os.setsid() 
        os.umask(0) 
    
        self._fork(2)
        
        # write pidfile
        atexit.register(self.remove_pid)
        try:
            self.pidfile.create()
        except RuntimeError, err:
            logging.error('service.daemonize(), %s' % str(err))
            return False
        logging.info('service.daemonize(), process [%s] started' % self.process.__name__)
        return True
    
    def remove_pid(self):
        if self.pidfile.validate():
            self.pidfile.unlink()
        logging.info('service.remove_pid(), service was stopped')

    def start(self):
        """
        Start the service
        """
        # Check for a pidfile to see if the service already runs
        if self.pidfile.validate():
            message = "service.start(), pidfile %s exists. Service is running already\n"
            logging.error(message % self.pidfile.pid)
            sys.exit(1)
            
        # Start the service
        if self.daemonize():
            self.process().run()

    def stop(self):
        """
        Stop the service
        """
        # Get the pid from the pidfile
        try:
            pf = file(self.__pidfile,'r')
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            pid = None
    
        if not pid:
            message = "service.stop(), pidfile %s does not exist. Service is not running\n"
            # sys.stderr.write(message % self.__pidfile)
            logging.error(message % self.__pidfile)
            return # not an error in a restart

        # Try killing the service process    
        try:
            while 1:
                os.kill(pid, SIGTERM)
                time.sleep(0.1)
        except OSError, err:
            err = str(err)
            if err.find("No such process") > 0:
                if os.path.exists(self.__pidfile):
                    os.remove(self.__pidfile)
            else:
                loggin.error('service.stop(), %s' % str(err))
                raise OSError(err)
        logging.info('service.stop(), service [%s] was stopped' % pid)

    def restart(self):
        """
        Restart the service
        """
        logging.info('service.restart(), service restarting')
        self.stop()
        self.start()
        logging.info('service.restart(), service restarted')




    
        
