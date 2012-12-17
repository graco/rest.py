#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='rest.py',
    version='0.0.1',
    description='An easy way to build RESTful services.',
    author='Kevin Conway',
    url='http://github.com/kevinconway/rest.py',
    license='MIT',
    platforms=['any'],
    packages=['rest', 'rest.middleware'],
    install_requires=(
            'werkzeug'
    )
)
