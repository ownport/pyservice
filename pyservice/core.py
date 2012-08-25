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
from .utils import logging_file_descriptors

sys.path.insert(0, os.getcwd())

# -----------------------------------------------------
#   classes
# -----------------------------------------------------
class Process(object):
    
    # TODO add support to logging process by own name
    
    pidfile = None  # Override this field for your class
    logfile = None  # Override this field for your class
    
    def __init__(self):
        atexit.register(self.do_stop())
    
    def do_start(self):
        ''' You should override this method when you subclass Process. 
        It will be called before the process will be runned via Service class. '''
        pass

    def do_stop(self):
        ''' You should override this method when you subclass Process. 
        It will be called after the process has been stopped or interupted by 
        signal.SIGTERM'''
        pass
    
    def run(self):
        '''
        You should override this method when you subclass Process. 
        It will be called after the process has been daemonized by 
        start() or restart() via Service class.
        '''
        pass

class Service(object):
    ''' Service class  '''
    
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
        '''
        do the UNIX double-fork magic, see Stevens' "Advanced 
        Programming in the UNIX Environment" for details (ISBN 0201563177)
        http://www.erlenstar.demon.co.uk/unix/faq_2.html#SEC16
        '''

        def _maxfd(limit=1024):
            ''' Use the getrlimit method to retrieve the maximum file 
            descriptor number that can be opened by this process. If 
            there is not limit on the resource, use the default value
            
            limit - default maximum for the number of available file descriptors.
            '''
            maxfd = resource.getrlimit(resource.RLIMIT_NOFILE)[1]
            if maxfd == resource.RLIM_INFINITY:
                return limit
            else:
                return maxfd
        
        def _devnull(default="/dev/null"):
            # The standard I/O file descriptors are redirected to /dev/null by default.
            if hasattr(os, "devnull"):
                return os.devnull
            else:
                return default

        def _close_fds(preserve=None):
            preserve = preserve or []
            for fd in xrange(0, _maxfd()):
                if fd not in preserve:
                    try:
                        os.close(fd)
                    except OSError: # fd wasn't open to begin with (ignored)
                        pass

        pid = self._fork(1) # first fork
        if pid == 0: # the first child
            os.setsid()
            pid = self._fork(2)
            if pid == 0: # the second child
                os.chdir("/") 
                os.umask(0) 
            else:
                os._exit(0)
            _close_fds(logging_file_descriptors())
        else:
            os._exit(0)             

        os.open(_devnull(), os.O_RDWR)
        os.dup2(0, 1)			# standard output (1)
        os.dup2(0, 2)			# standard error (2)

        return True
    
    def remove_pid(self):
        if self.pidfile.validate():
            self.pidfile.unlink()
        logging.info('service.remove_pid(), service was stopped')

    def start(self):
        '''
        Start the service
        '''
        
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
            user_process = self.process()
            if getattr(user_process, 'do_start'):
                user_process.do_start()
            user_process.run()

    def stop(self):
        '''
        Stop the service
        '''
        pid = self.pidfile.validate()
        if not pid:
            message = "service.stop(), pidfile %s does not exist. Service is not running"
            logging.error(message % self.pidfile.fname)
            return # not an error in a restart

        # Try killing the service process    
        try:
            while 1:
                os.kill(pid, signal.SIGTERM)
                time.sleep(0.1)
        except OSError, err:
            err = str(err)
            if err.find("No such process") > 0:
                if self.pidfile.validate():
                    self.pidfile.unlink()
            else:
                loggin.error('service.stop(), %s' % str(err))
                raise OSError(err)
        logging.info('service.stop(), service [%s] was stopped' % pid)




    
        
