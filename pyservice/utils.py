''' utils '''

import os
import sys
import runpy
import errno
import logging

#
#   Logging
#

# TODO make logging more useful for debugging

DEFAULT_FORMAT = "%(asctime)s pid:%(process)d <%(levelname)s> %(message)s"

def set_logging(logfile, output_format=DEFAULT_FORMAT, level=logging.DEBUG):
    ''' set logging '''
    
    logging.basicConfig(format=output_format, filename = logfile, level=logging.DEBUG)

def load_process(process_path):
    ''' load process 
    
    PEP 338 - Executing modules as scripts
    http://www.python.org/dev/peps/pep-0338
    '''
    if '.' not in process_path:
        raise RuntimeError("Invalid process path")

    module_name, process_name = process_path.rsplit('.', 1)
    try:
        try:
            module = runpy.run_module(module_name)
        except ImportError:
            module = runpy.run_module(module_name + ".__init__")
    except ImportError, e:
        import traceback, pkgutil
        tb_tups = traceback.extract_tb(sys.exc_info()[2])
        if pkgutil.__file__.startswith(tb_tups[-1][0]):
            # If the bottommost frame in our stack was in pkgutil,
            # then we can safely say that this ImportError occurred
            # because the top level class path was not found.
            raise RuntimeError("Unable to load process path: {}:\n{}".format(process_path, e))
        else:
            # If the ImportError occurred further down,
            # raise original exception.
            raise
    try:
        return module[process_name]
    except KeyError, e:
        raise RuntimeError("Unable to find process in module: {}".format(process_path))
        
#
#   Pidfile
#

class Pidfile(object):
    ''' Manage a PID file '''

    def __init__(self, fname):
        self.fname = fname
        self.pid = None

    def create(self):
        ''' create pid file '''
        pid = self.validate()
        if pid:
            if pid == os.getpid():
                return
            raise RuntimeError("Already running on PID %s " \
                "(or pid file '%s' is stale)" % (os.getpid(), self.fname))            
                
        self.pid = os.getpid()

        # Write pidfile
        fdir = os.path.dirname(self.fname)
        if fdir and not os.path.isdir(fdir):
            raise RuntimeError(
                    "%s doesn't exist. Can't create pidfile %s" % (fdir, self.fname))

        pfile = open(self.fname,'w')
        pfile.write("%s\n" % self.pid)
        pfile.close()

        # set permissions to -rw-r--r-- 
        os.chmod(self.fname, 420)
            
    def unlink(self):
        """ delete pidfile"""
        try:
            with open(self.fname, "r") as f:
                pid_in_file =  int(f.read() or 0)

            if pid_in_file == self.pid:
                os.unlink(self.fname)
        except:
            pass

    def validate(self):
        """ Validate pidfile and make it stale if needed"""
        # TODO reveiw the code
        if not self.fname:
            return
        try:
            with open(self.fname, "r") as f:
                wpid = int(f.read() or 0)

                if wpid <= 0:
                    return

                try:
                    os.kill(wpid, 0)
                    return wpid
                except OSError, e:
                    if e[0] == errno.ESRCH:
                        return
                    raise
        except IOError, e:
            if e[0] == errno.ENOENT:
                return
            raise


