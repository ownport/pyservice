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
    try:
        if args.action in "start stop restart reload status".split():
            if not args.process:
                parser.error("You need to specify a process for {}".format(args.action))
            getattr(ServiceControl(), args.action)(args.process)
        else:
            print 'Please specify action for {}\n'.format(args.process)
            parser.print_help()
    except RuntimeError, e:
        parser.error(e)    
    
class ServiceControl(object):
    
    def start(self, process_path):
        ''' start process '''
        
        print "Starting process with {}...".format(process_path)
        process = load_process(process_path)
        if callable(process):
            pyservice.core.Service(process).start()
        else:
            raise RuntimeError("The process {} is not valid".format(process_path))    
                
    def stop(self, process_path):
        if self._validate(pid):
            print "Stopping process {}...".format(pid)
            os.kill(pid, STOP_SIGNAL)
            
    def restart(self, process_path):
        self.stop(resolve_pid(target=target))
        self.start(target)

    def status(self, process_path):
        if self._validate(pid):
            print "Process is running as {}.".format(pid)

    def _validate(self, process_path):
        try:
            os.kill(pid, 0)
            return pid
        except (OSError, TypeError):
            print "Process is NOT running."


