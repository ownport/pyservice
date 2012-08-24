pyservice
=========

simple library to make service on python more easy. That's experimental project. Ideas were taken from [progrium/ginkgo](https://github.com/progrium/ginkgo), [daemon.py for python 2.x](http://www.jejik.com/articles/2007/02/a_simple_unix_linux_daemon_in_python/) and [daemon.py for python 3.x](http://www.jejik.com/files/examples/daemon3x.py). 

The pyservice is responsible for creating a "container" to run services in, and tools to manage that container. The container is itself a service based on a class called `Process`, which is intended to model the running process that contains the service. The process service takes an application service to run and then initializes the process to daemonize. 

The "ControlInterface" class models the commands you can use to start or control a daemonized service. This is exposed via one command line utilities "pyservice" which have the entry point defined in this module.

The runner module (runner.py) and command line utilities (pyservice) are completely optional. You can always just write your own Python script or console command that takes your application service.


```
$ python -m pyservice tests.processes.simple_process.SimpleProcess start
```


### TODO

 - handle cases correctly when process is killed

### Links

 - [How do I get my program to act like a daemon?](http://www.svbug.com/documentation/comp.unix.programmer-FAQ/faq_2.html#SEC16)
 - [PEP: 3143, Standard daemon process library](http://www.python.org/dev/peps/pep-3143/)
 - [Building a python daemon process](http://www.gavinj.net/2012/06/building-python-daemon-process.html)
 - [Creating a daemon the Python way (Python recipe)](http://code.activestate.com/recipes/278731-creating-a-daemon-the-python-way/)
