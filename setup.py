#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup, find_packages
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


import pytimekr
setup(
    name='pytimekr',
    version=pytimekr.__version__,
    description='PyTime fork for Korean',
    long_description=long_description,
    url='https://github.com/Parkayun/PyTimeKR',
    author='Parkayun',
    author_email='iamparkayun@gmail.com',
    license='MIT',
    keywords='datetime time datetime timeparser korea holiday',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    package_data={'': ['README.md']},
    # tests_require=['coverage'],
    # extras_require={
    #     'coveralls': ['coveralls']
    # },
    install_requires=[
        'lunardate>=0.1.5',
    ],
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
