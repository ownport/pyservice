pyservice
=========

## Introduction

simple library to make service on python more easy. That's *experimental* project. Ideas were taken from [progrium/ginkgo](https://github.com/progrium/ginkgo), [daemon.py for python 2.x](http://www.jejik.com/articles/2007/02/a_simple_unix_linux_daemon_in_python/) and [daemon.py for python 3.x](http://www.jejik.com/files/examples/daemon3x.py). 

The pyservice is responsible for creating a "container" to run services in, and tools to manage that container. The container is itself a service based on a class called `Process`, which is intended to model the running process that contains the service. The pyservice initializes the process to daemonize then the process takes an application service to run. 

## Installation

To install pyservice just download pyservice.py and place it in your project directory. There are no dependencies other than the Python Standard Library.

## How to start to use

The example of [simple process](https://github.com/ownport/pyservice/blob/master/tests/processes/simple_process.py)
```python
import os
import time
import pyservice

class SimpleProcess(pyservice.Process):
    
    pidfile = os.path.join(os.getcwd(), 'tests/run/simple_process.pid')
    logfile = os.path.join(os.getcwd(), 'tests/log/simple_process.log')
    
    def run(self):
        time.sleep(10)
```

To run this process as service you just need to type in command line 
```
$ python -m pyservice tests.processes.simple_process.SimpleProcess start
```

## Details

The "ControlInterface" class models the commands you can use to start or control a daemonized service. This is exposed via one command line utilities "pyservice" which have the entry point defined in this module.

The runner module and command line utilities are completely optional. You can always just write your own Python script or console command that takes your application service.

## Examples

 - [How to run built-in HTTP server of bottle.py as service in background](https://github.com/ownport/pyservice/tree/master/examples/bottlepy-daemon)

### Links

 - [How do I get my program to act like a daemon?](http://www.svbug.com/documentation/comp.unix.programmer-FAQ/faq_2.html#SEC16)
 - [PEP: 3143, Standard daemon process library](http://www.python.org/dev/peps/pep-3143/)
 - [Building a python daemon process](http://www.gavinj.net/2012/06/building-python-daemon-process.html)
 - [Creating a daemon the Python way (Python recipe)](http://code.activestate.com/recipes/278731-creating-a-daemon-the-python-way/)
 - [start-stop-daemon](http://man.he.net/man8/start-stop-daemon)
