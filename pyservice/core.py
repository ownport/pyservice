''' core '''

import os
import sys
import time
import signal
import atexit
import logging
import resource

from .utils import Pidfile
from .utils import set_logging

SIGNAL_STOP = signal.SIGTERM
SIGNAL_RELOAD = signal.SIGHUP

sys.path.insert(0, os.getcwd())

# -----------------------------------------------------
#   classes
# -----------------------------------------------------
class Process(object):
    
    # TODO add support to logging process by own name
    
    pidfile = None  # Override this field for your class
    logfile = None  # Override this field for your class
    
    def run(self):
        """
        You should override this method when you subclass Process. 
        It will be called after the process has been daemonized by 
        start() or restart() via Service class.
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
            self.logger = logging.getLogger(process.__name__)          


    def _fork(self, fid):
        ''' fid - fork id'''
        
        try: 
            pid = os.fork() 
        except OSError, e: 
            logging.error(
                "service._fork(), fork #%d failed: %d (%s)\n" % (fid, e.errno, e.strerror))
            raise OSError(e)  
        return pid
    
    def daemonize(self):
        """
        do the UNIX double-fork magic, see Stevens' "Advanced 
        Programming in the UNIX Environment" for details (ISBN 0201563177)
        http://www.erlenstar.demon.co.uk/unix/faq_2.html#SEC16
        """
        # TODO handle file descriptors, logging
        
        # Default maximum for the number of available file descriptors.
        MAXFD = 1024

        # The standard I/O file descriptors are redirected to /dev/null by default.
        if (hasattr(os, "devnull")):
            REDIRECT_TO = os.devnull
        else:
            REDIRECT_TO = "/dev/null"

        pid = self._fork(1) # first fork
        if pid == 0: # the first child
            os.setsid()
            pid = self._fork(2)
            if pid == 0: # the second child
                os.chdir("/") 
                os.umask(0) 
            else:
                os._exit(0)
        else:
            os._exit(0)             

        os.open(REDIRECT_TO, os.O_RDWR)	# standard input (0)
        os.dup2(0, 1)			# standard output (1)
        os.dup2(0, 2)			# standard error (2)

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
        current_pid = self.pidfile.validate()
        if current_pid:
            message = "service.start(), pidfile %s exists. Service is running already"
            logging.error(message % current_pid)
            return

        # Start the service
        if self.daemonize():
            # create pid file
            try:
                self.pidfile.create()
            except RuntimeError, err:
                logging.error('service.start(), %s' % str(err))
                return
            # activate handler for stop the process
            atexit.register(self.remove_pid)
            
            logging.info('service.start(), process [%s] started' % self.process.__name__)
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




    
        
