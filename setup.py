from setuptools import setup, find_packages


with open("./requirements.txt") as f:
    requirements = f.read().splitlines()

with open("ImageRobot/version.py") as version_file:
    VERSION = version_file.read().strip().split('"')[1]


setup(
    name                    = "ImageRobot",
    version                 = VERSION,
    packages                = find_packages(),
    url                     = "https://github.com/Atyors/ImageRobot",
    author                  = "Rouyan Thi",
    author_email            = "rouyanthi@gmail.com",
    description             = "A library used to do image recognition.",
    long_description        = open('README.md').read(),
    include_package_data    = True,
    classifiers             = [
                                "Programming Language :: Python",
                                "Development Status :: 5 - Production/Stable",
                                "Natural Language :: English",
                                "Operating System :: OS Independent",
                                "Programming Language :: Python :: 3.7",
                                "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
                            ],
    install_requires        = requirements,
)
