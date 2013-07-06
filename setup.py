import re
import os
import pyservice
from setuptools import setup

setup(
    name = "pyservice",
    version = pyservice.__version__,
    author = re.sub(r'\s+<.*', r'', pyservice.__author__),
    author_email = re.sub(r'(^.*<)|(>.*$)', r'', pyservice.__author__),
    url = 'https://github.com/ownport/pyservice',
    description = ("simple library to make service on python more easy"),
    long_description = open('README.md').read(),
    license = "BSD",
    keywords = "python service daemon",
    py_modules = ['pyservice'],
    classifiers = [
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Topic :: Software Development :: Libraries :: Python Modules',
        
    ],
    entry_points={
        'console_scripts': ['pyservice = pyservice.runner:run_service']},
)

