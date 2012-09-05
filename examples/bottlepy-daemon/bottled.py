#!/usr/bin/env python

import os
import sys
import logging

from packages import bottle
from packages import pyservice

# monkey patching for BaseHTTPRequestHandler.log_message
def log_message(obj, format, *args):
    logging.info("%s %s" % (obj.address_string(), format%args))

# Application
@bottle.route('/')
def index():
    return 'BottleProcess'

# Process to run
class BottleProcess(pyservice.Process):

    pidfile = os.path.join(os.getcwd(), 'run/bottle.pid')
    logfile = os.path.join(os.getcwd(), 'log/bottle.log')

    def __init__(self):
        super(BottleProcess, self).__init__()
        
        from BaseHTTPServer import BaseHTTPRequestHandler
        BaseHTTPRequestHandler.log_message = log_message
            
    def run(self):
        logging.info('Bottle {} server starting up'.format(bottle.__version__))
        bottle.run(host='localhost', port=8080)

if __name__ == '__main__':

    if len(sys.argv) == 2 and sys.argv[1] in 'start stop restart status'.split():
        pyservice.service('bottled.BottleProcess', sys.argv[1])
    else:
        print 'usage: bottled <start,stop,restart,status>'

