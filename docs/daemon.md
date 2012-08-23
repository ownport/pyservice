# Creating a daemon the Python way (Python recipe)

Original port on [ActiveState.com](http://code.activestate.com/recipes/278731-creating-a-daemon-the-python-way/)

The Python way to detach a process from the controlling terminal and run it in the background as a daemon.

Configurable daemon behaviors:

 - The current working directory set to the "/" directory.
 - The current file creation mode mask set to 0.
 - Close all open files (1024). 
 - Redirect standard I/O streams to "/dev/null".

A failed call to fork() now raises an exception.

References:

 - Advanced Programming in the Unix Environment: W. Richard Stevens
 -  [Unix Programming Frequently Asked Questions](http://www.erlenstar.demon.co.uk/unix/faq_toc.html)
 
```python
# Default daemon parameters.
# File mode creation mask of the daemon.
UMASK = 0

# Default working directory for the daemon.
WORKDIR = "/"

# Default maximum for the number of available file descriptors.
MAXFD = 1024

# The standard I/O file descriptors are redirected to /dev/null by default.
if (hasattr(os, "devnull")):
   REDIRECT_TO = os.devnull
else:
   REDIRECT_TO = "/dev/null"
```

Detach a process from the controlling terminal and run it in the background as a daemon.

```python
try:
    # Fork a child process so the parent can exit.  This returns control to
    # the command-line or shell.  It also guarantees that the child will not
    # be a process group leader, since the child receives a new process ID
    # and inherits the parent's process group ID.  This step is required
    # to insure that the next call to os.setsid is successful.
    pid = os.fork()
except OSError, e:
    raise Exception, "%s [%d]" % (e.strerror, e.errno)
```

