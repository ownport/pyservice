# How to use bottle.py with pyservice

Bottle is a fast and simple micro-framework for small web applications. It offers request dispatching (URL routing) with URL parameter support, templates, a built-in HTTP Server and adapters for many third party WSGI/HTTP-server and template engines - all in a single file and with no dependencies other than the Python Standard Library. Homepage and documentation: [http://bottlepy.org/](http://bottlepy.org/) License: MIT

`bottled.py` allows to run built-in HTTP Server of bottle.py as a service. There's not too much logic - just test page 'BottleProcess' is available by http://127.0.0.1:8080 but it can be extended easy. For more details how to develop web applications with bottle.py please read [documentation](http://bottlepy.org/docs/dev/)

There's two ways how to control bottle.py HTTP server:
 - via pyservice console
 - or directly via bottled.py

*Note!* All below commands should be executed from examples/bottlepy-daemon directory
 
To start bottled.py via pyservice console:
```
$ python -m packages.pyservice bottled.BottleProcess start
Starting process with BottleProcess...
$
``` 
or 
```
$ python bottled.py start
Starting process with BottleProcess...
$
``` 

Check current status
```
$ python -m packages.pyservice bottled.BottleProcess status
Process BottleProcess is running, pid: 27688
$
``` 
or 
```
$ python bottled.py status
Process BottleProcess is running, pid: 27706
$
``` 

Restart the bottled.py process
```
$ python -m packages.pyservice bottled.BottleProcess restart
Stopping process BottleProcess...
Starting process with BottleProcess...
$
``` 
or 
```
$ python bottled.py restart
Stopping process BottleProcess...
Starting process with BottleProcess...
$
``` 

Stop the process
```
$ python -m packages.pyservice bottled.BottleProcess stop
Stopping process BottleProcess...
$
``` 
or 
```
$ python bottled.py stop
Stopping process BottleProcess...
$
``` 


