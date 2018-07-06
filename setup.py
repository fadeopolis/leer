#!/usr/bin/env python3

from distutils.core import setup

setup(
  name='leer',
  version='1.0',
  description='execute a program periodically, showing output fullscreen (and allow scrolling in the output)',
  author='Fabian Gruber',
  license='BSD 3-Clause License',
  url='https://github.com/fadeopolis/leer',
  scripts=['scripts/leer'],
)
