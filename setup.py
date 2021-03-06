#!/usr/bin/env python
import os
import re

from setuptools import setup

INSTALL_REQUIRES = ["docopt"]
TEST_REQUIRES = ["pytest"]


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.rst")) as f:
    long_description = f.read()


with open(os.path.join(here, "picklecat.py")) as f:
    matches = re.findall(r"(__.+__) = \"(.*)\"", f.read())
    for var_name, var_value in matches:
        globals()[var_name] = var_value


setup(
    name=__title__,
    version=__version__,
    description=__description__,
    long_description=long_description,
    py_modules=["picklecat"],
    install_requires=INSTALL_REQUIRES,
    entry_points={"console_scripts": [
        "picklecat = picklecat:main",
    ]},
    license=__license__,
    tests_require=TEST_REQUIRES,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
    ],
)
