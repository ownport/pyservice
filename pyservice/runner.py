""" pyservice runner """

import sys
import pyservice

from pyservice.utils import load_process


def run_service():

    import argparse

    parser = argparse.ArgumentParser(prog="pyservice", add_help=False)
    parser.add_argument("-v", "--version",
        action="version", version="%(prog)s, v.{}".format(pyservice.__version__))
    parser.add_argument("-h", "--help", 
        action="store_true", help="show program's help text and exit")
    parser.add_argument("process", nargs='?', help="""
        process class path to run (modulename.ProcessClass) or
        configuration file path to use (/path/to/config.py)
        """.strip())
    parser.add_argument("action", nargs='?', 
        choices="start stop restart reload status".split()) 
    
    try:        
        args = parser.parse_args()
    except TypeError:
        parser.print_help()
        return
        
    if args.help:
        parser.print_help()
        return

    try:
        if args.process and args.action in "start stop restart reload status".split():
            if not args.process:
                parser.error("You need to specify a process for {}".format(args.action))
            getattr(ServiceControl(args.process), args.action)()
        else:
            parser.print_help()
    except RuntimeError, e:
        parser.error(e)    
    
class ServiceControl(object):
    
    def __init__(self, process_path):
        self.process = load_process(process_path)
        if not callable(self.process):
            raise RuntimeError("The process {} is not valid".format(self.process_path))    
    
    def start(self):
        
        print "Starting process with {}...".format(self.process.__name__)
        pyservice.core.Service(self.process).start()
                
    def stop(self):

        print "Stopping process {}...".format(self.process.__name__)
        pyservice.core.Service(self.process).stop()
            
    def restart(self):

        print 'Restarting {} process'.format(self.process.__name__)
        self.stop()
        self.start()
        print 'Process {} was restarted'.format(self.process.__name__)

    def status(self, process_path):

        if self._validate(pid):
            print "Process is running as {}.".format(pid)

    def _validate(self, process_path):
        try:
            os.kill(pid, 0)
            return pid
        except (OSError, TypeError):
            print "Process is NOT running."


