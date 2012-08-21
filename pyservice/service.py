#!/usr/bin/env python
# -*- codeing: utf-8 -*-
#
#   service.py
#
#   Below is the Service class. To use it, simply subclass it and implement the run() method.
#

import os
import sys
import time
import signal
import atexit
import logging
import argparse

SIGNAL_STOP = signal.SIGTERM
SIGNAL_RELOAD = signal.SIGHUP

sys.path.insert(0, os.getcwd())

logger = logging.getLogger(__name__)

def run_service():
    parser = argparse.ArgumentParser(prog="pyservice", add_help=False)
    parser.add_argument("-v", "--version",
        action="version", version="%(prog)s {}".format(pyservice.__version__))
    parser.add_argument("-h", "--help", action="store_true", help="""
        show program's help text and exit
        """.strip())
    parser.add_argument("-d", "--daemonize", action="store_true", help="""
        daemonize the service process
        """.strip())
    parser.add_argument("target", nargs='?', help="""
        service class path to run (modulename.ServiceClass) or
        configuration file path to use (/path/to/config.py)
        """.strip())
    args = parser.parse_args()
    if args.help:
        parser.print_help()
        if args.target:
            print # blank line
            try:
                app = setup_process(args.target)
                app.config.print_help()
            except RuntimeError, e:
                parser.error(e)
    else:
        if args.target:
            try:
                ControlInterface().start(args.target, args.daemonize)
            except RuntimeError, e:
                parser.error(e)
        else:
            parser.print_usage()

# -----------------------------------------------------
#   classes
# -----------------------------------------------------
class Service(object):
    """
    A generic service class.
    
    Usage: subclass the Service class and override the run() method
    """
    def __init__(self, pidfile, logfile=None):
        '''
        pidfile
        logfile
        '''
        self.__pidfile = pidfile
        try:
            logging.basicConfig(format='%(asctime)s pid:%(process)d <%(levelname)s> %(message)s', 
                                filename = logfile, 
                                level=logging.DEBUG)
        except IOError, e:
            print str(e)
            sys.exit(1)
    
    def daemonize(self):
        """
        do the UNIX double-fork magic, see Stevens' "Advanced 
        Programming in the UNIX Environment" for details (ISBN 0201563177)
        http://www.erlenstar.demon.co.uk/unix/faq_2.html#SEC16
        """
        try: 
            pid = os.fork() 
            if pid > 0:
                # exit first parent
                sys.exit(0) 
        except OSError, e: 
            # sys.stderr.write("fork #1 failed: %d (%s)\n" % (e.errno, e.strerror))
            logging.error("service.daemonize(), fork #1 failed: %d (%s)\n" % (e.errno, e.strerror))
            sys.exit(1)
    
        # decouple from parent environment
        os.chdir("/") 
        os.setsid() 
        os.umask(0) 
    
        # do second fork
        try: 
            pid = os.fork() 
            if pid > 0:
                # exit from second parent
                sys.exit(0) 
        except OSError, e: 
            # sys.stderr.write("fork #2 failed: %d (%s)\n" % (e.errno, e.strerror))
            logging.error("service.daemonize(), fork #2 failed: %d (%s)\n" % (e.errno, e.strerror))
            sys.exit(1) 
        
        # write pidfile
        atexit.register(self.remove_pid)
        pid = str(os.getpid())
        try:
            pfile = open(self.__pidfile,'w')
            pfile.write("%s\n" % pid)
            pfile.close()
        except IOError, e:
            logging.error('service.daemonize(), %s' % str(e))
            sys.exit(1)
        logging.info('service.daemonize(), service [%s] started, pidfile: %s' % (pid, self.__pidfile))
    
    def remove_pid(self):
        if os.path.isfile(self.__pidfile):
            os.remove(self.__pidfile)
        logging.info('service.remove_pid(), service was stopped')

    def start(self):
        """
        Start the service
        """
        # Check for a pidfile to see if the service already runs
        try:
            pf = file(self.__pidfile,'r')
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            pid = None
        except ValueError:
            pid = None
    
        if pid:
            message = "service.start(), pidfile %s already exist. Service is already running\n"
            # sys.stderr.write(message % self.__pidfile)
            logging.error(message % self.__pidfile)
            sys.exit(1)
        
        # Start the service
        self.daemonize()
        self.run()

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
                sys.exit(1)
        logging.info('service.stop(), service [%s] was stopped' % pid)

    def restart(self):
        """
        Restart the service
        """
        logging.info('service.restart(), service restarting')
        self.stop()
        self.start()
        logging.info('service.restart(), service restarted')

    def run(self):
        """
        You should override this method when you subclass Service. It will be called after the process has been
        daemonized by start() or restart().
        """
        pass



    
        
