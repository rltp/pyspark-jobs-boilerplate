#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
from setuptools import find_packages

setup(
    name='pipeline',
    version='1.0.0',
    packages=find_packages(exclude=["*_tests"]),
    include_package_data=True,
    license='MIT license',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires = [
        'numpy'
    ],
    extras_require={
        'dev': [
            'pylint',
            'coverage',
            'tox',
            'twine',
            'pyspark==3.0.1'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)
