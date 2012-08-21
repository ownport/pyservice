pyservice
=========

simple library to make service on python more easy. That's experimental project. Ideas were taken from [progrium/ginkgo](https://github.com/progrium/ginkgo), [daemon.py for python 2.x](http://www.jejik.com/articles/2007/02/a_simple_unix_linux_daemon_in_python/) and [daemon.py for python 3.x](http://www.jejik.com/files/examples/daemon3x.py). 

The pyservice is responsible for creating a "container" to run services in, and tools to manage that container. The container is itself a service based on a class called `Process`, which is intended to model the running process that contains the service. The process service takes an application service to run and then initializes the process to daemonize. 

The "ControlInterface" class models the commands you can use to start or control a daemonized service. This is exposed via one command line utilities "pyservice" which have the entry point defined in this module.

The runner module (service.py) and command line utilities (pyservice) are completely optional. You can always just write your own Python script or console command that takes your application service.


### TODO

 - handle cases correctly when process is killed

### Links


[How do I get my program to act like a daemon?](http://www.svbug.com/documentation/comp.unix.programmer-FAQ/faq_2.html#SEC16)

