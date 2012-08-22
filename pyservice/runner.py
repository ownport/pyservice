""" pyservice runner """

import sys
import pyservice

def run_service():

    import argparse

    parser = argparse.ArgumentParser(prog="pyservice", add_help=False)
    parser.add_argument("-v", "--version",
        action="version", version="%(prog)s, v.{}".format(pyservice.__version__))
    parser.add_argument("-h", "--help", action="store_true", help="""
        show program's help text and exit
        """.strip())
    parser.add_argument("-p", "--pid", help="""
        pid or pidfile to use instead of target
        """.strip())
    parser.add_argument("target", nargs='?', help="""
        service class path to run (modulename.ServiceClass) or
        configuration file path to use (/path/to/config.py)
        """.strip())
    parser.add_argument("action",
        choices="start stop restart reload status".split()) 
    
    try:        
        args = parser.parse_args()
    except TypeError:
        parser.print_help()
        return
    
    if args.help:
        parser.print_help()
    elif args.pid and args.target:
        parser.error("You cannot specify both a target and a pid")
    try:
        if args.action in "start stop restart reload status".split():
            if not args.target or not args.pid:
                parser.error("You need to specify a target or a pid for {}".format(args.action))
            getattr(ControlInterface(), args.action)(resolve_pid(args.pid, args.target))
    except RuntimeError, e:
        parser.error(e)    

def resolve_pid(pid=None, target=None):
    if pid and not os.path.exists(pid):
        return int(pid)
    if target is not None:
        # TODO get pid from process code
        # setup_process(target, daemonize=True)
        # pid = ginkgo.settings.get("pidfile")
        pass
    if pid is not None:
        if os.path.exists(pid):
            with open(pid, "r") as f:
                pid = f.read().strip()
            return int(pid)
        else:
            return
    raise RuntimeError("Unable to resolve pid from {}".format(pid or target))
    
class ControlInterface(object):
    
    def start(self, target):
        pass
    
    def restart(self, target):
        pass
    
    def stop(self, pid):
        pass

    def reload(self, pid):
        pass

    def status(self, pid):
        pass
    

if __name__ == '__main__':
    run_service()            
