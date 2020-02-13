from setuptools import setup, find_packages
import ImageRobot

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name                    = "ImageRobot",
    version                 = ImageRobot.__version__,
    packages                = find_packages(),
    url                     = "https://github.com/Atyors/ImageRobot",
    author                  = "Rouyan Thi",
    author_email            = "rouyanthi@gmail.com",
    description             = "A library used to do image recognition.",
    long_description        = open('README.md').read(),
    include_package_data    = True,
    classifiers             = [
                                "Programming Language :: Python",
                                "Development Status :: 5 - Stable",
                                "Natural Language :: English",
                                "Operating System :: OS Independent",
                                "Programming Language :: Python :: 3.7",
                                "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
                            ],
    install_requires        = requirements,
)
