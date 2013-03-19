# PyService API

## Process

- `do_start()`

    You should override this method when you subclass Process. It will be called before the process will be runned via Service class.

- `do_stop()`

    You should override this method when you subclass Process. It will be called after the process has been stopped or interupted by signal.SIGTERM
    
- `run()`

    You should override this method when you subclass Process. It will be called after the process has been daemonized by start() or restart() via Service class.

## Service

- `daemonize()`

    do the UNIX double-fork magic, see Stevens' ["Advanced Programming in the UNIX Environment" for details (ISBN 0201563177)](http://www.erlenstar.demon.co.uk/unix/faq_2.html#SEC16)

- `remove_pid()`

    remove pid file

- `start()`

    start the service

- `stop()`

    stop the service

## ServiceControl

- `start()`

    start the service

- `stop()`

    stop the service

- `restart()`

    restart the service

- `status()`

    get the service status

## Pidfile

- `__init__(filaname)`

    The constructor. filename is filename of PID file


- `create()`

    create PID file

- `unlink()`

    delete PID file

- `validate()`

    validate PID file


## Utilities

- `set_logging(process_name, logfile, output_format=DEFAULT_FORMAT, level=logging.DEBUG)`

    set logging

- `logging_file_descriptors()`

    logging file descriptors are used in core.Service.daemonize()

- `load_process(process_path)`

    Load process. [PEP 338](http://www.python.org/dev/peps/pep-0338) - Executing modules as scripts

- `service(process=None, action=None)`

    control service











