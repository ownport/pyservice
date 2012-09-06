# How to use bottle.py with pyservice

Bottle is a fast and simple micro-framework for small web applications. It offers request dispatching (URL routing) with URL parameter support, templates, a built-in HTTP Server and adapters for many third party WSGI/HTTP-server and template engines - all in a single file and with no dependencies other than the Python Standard Library. Homepage and documentation: [http://bottlepy.org/](http://bottlepy.org/) License: MIT

`bottled.py` allows to run built-in HTTP Server of bottle.py as a service. There's not too much logic - just test page 'BottleProcess' is available by http://127.0.0.1:8080 but it can be extended easy. For more details how to develop web applications with bottle.py please read [documentation](http://bottlepy.org/docs/dev/)

There's two ways how to control bottle.py HTTP server:
 - via pyservice console
 - or directly via bottled.py

*Note!* All below commands should be executed from examples/bottlepy-daemon directory
``` 
$ python -m packages.pysevice bottled.BottleProcess
usage: pyservice [-v] [-h] [process] [{start,stop,restart,status}]

positional arguments:
  process               process class path to run (modulename.ProcessClass) or
                        configuration file path to use (/path/to/config.py)
  {start,stop,restart,status}

optional arguments:
  -v, --version         show program's version number and exit
  -h, --help            show program's help text and exit
```
Or
```
$ python bottled.py 
usage: bottled <start,stop,restart,status>
```

