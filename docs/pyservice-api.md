# PyService API

## Process

- `do_start()`
    ''' You should override this method when you subclass Process. 
    It will be called before the process will be runned via Service class. '''
    pass

- `do_stop()`
    ''' You should override this method when you subclass Process. 
    It will be called after the process has been stopped or interupted by 
    signal.SIGTERM'''
    pass
    
- `run()`
    You should override this method when you subclass Process. 
    It will be called after the process has been daemonized by 
    start() or restart() via Service class.


