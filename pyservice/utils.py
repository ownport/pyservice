''' utils '''

import os
import errno
import logging

DEFAULT_FORMAT = "%(asctime)s pid:%(process)d/%(module)s <%(levelname)s> %(message)s"

def set_logging(logfile, output_format=DEFAULT_FORMAT, level=logging.DEBUG):
    ''' set logging '''
    
    logging.basicConfig(format=output_format, filename = logfile, level=logging.DEBUG)


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
            raise RuntimeError("%s doesn't exist. Can't create pidfile." % fdir)

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


