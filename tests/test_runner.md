# Runner (examples of usage + tests)

Before any tests or playing examples, the modules `pyservice.runner` and `sys` should be imported. Monkey patching is used for sys.exit to avoid exit from command
```
>>> import sys
>>> from pyservice import runner
>>> sys.stderr = sys.stdout
>>> sys.exit = lambda x:x
>>>
```
Show pyservice version with flag -v
```
>>> sys.argv = list()
>>> sys.argv.append('pyservice.py')
>>> sys.argv.append('-v')
>>> runner.run_service()
pyservice, v.0.2.1
usage: pyservice [-v] [-h] [process] [{start,stop,restart,reload,status}]
<BLANKLINE>
positional arguments:
  process               process class path to run (modulename.ProcessClass) or
                        configuration file path to use (/path/to/config.py)
  {start,stop,restart,reload,status}
<BLANKLINE>
optional arguments:
  -v, --version         show program's version number and exit
  -h, --help            show program's help text and exit

```
_Note_: Due to monkey patching is used for sys.exit, the result of run_service() is extended by common help printout. It's expected behaviour. TODO: review it to avoid in the future

Show pyservice version with flag --version
```
>>> sys.argv = list()
>>> sys.argv.append('pyservice.py')
>>> sys.argv.append('--version')
>>> runner.run_service()
pyservice, v.0.2.1
usage: pyservice [-v] [-h] [process] [{start,stop,restart,reload,status}]
<BLANKLINE>
positional arguments:
  process               process class path to run (modulename.ProcessClass) or
                        configuration file path to use (/path/to/config.py)
  {start,stop,restart,reload,status}
<BLANKLINE>
optional arguments:
  -v, --version         show program's version number and exit
  -h, --help            show program's help text and exit

```


