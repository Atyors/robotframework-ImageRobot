#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import ImageSearchLibrary

setup(
    name='ImageSearchLibrary',
    version=ImageSearchLibrary.__version__,
    packages=find_packages(),
    author="Sam et Max",
    author_email="lesametlemax@gmail.com",
    description="Proclame la bonne parole de sieurs Sam et Max",
    long_description=open('README.md').read(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 1 - Planning",
        "License :: OSI Approved",
        "Natural Language :: French",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Topic :: Communications",
    ],
)
