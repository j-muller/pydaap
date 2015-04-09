#!/usr/bin/env python

from setuptools import setup

import pydaap

setup(name='Pydaap',
      version=pydaap.__version__,
      description='Python library for parsing DAAP protocol',
      long_description=open('README.md').read(),
      author='Jeffrey Muller',
      url='https://github.com/j-muller/pydaap/',
      license='MIT',
      include_package_data=True,
)
