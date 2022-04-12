#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# TIME ： 2022-04-12
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("fourcats_connector/__init__.py", "r") as file:
    regex_version = r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]'
    version = re.search(regex_version, file.read(), re.MULTILINE).group(1)

with open("README.md", "rb") as file:
    readme = file.read().decode("utf-8")


setup(
    name="fourcats-connector",
    version=version,
    packages=["fourcats_connector"],
    description="A quick use tool for Python common connectors.",
    long_description=readme,
    long_description_content_type="text/x-rst",
    author="ShiWeiDong",
    url="https://github.com/FourCats-Py/FourCats-Connector",
    download_url="https://github.com/Delgan/loguru/archive/{}.tar.gz".format(version),
    keywords=["fourcats", "connect", "connector"],
    install_requires=["loguru>=0.6.0"],
    python_requires=">=3.5"
)
