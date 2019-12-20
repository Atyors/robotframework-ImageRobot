#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import ImageRobot

setup(
    name                    = "ImageRobot",
    version                 = ImageRobot.__version__,
    packages                = find_packages(),
    author                  = "Rouyan Thi",
    author_email            = "rouyanthi@gmail.com",
    description             = "A library used to do image recognition.",
    long_description        = open('README.md').read(),
    include_package_data    = True,
    classifiers             = [
                                "Programming Language :: Python",
                                "Development Status :: 1 - Planning",
                                "License :: OSI Approved",
                                "Natural Language :: English",
                                "Operating System :: OS Independent",
                                "Programming Language :: Python :: 2.7",
                                "Topic :: Communications",
                            ],
)
