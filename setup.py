#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# TIME ： 2022-04-12
from setuptools import setup, find_packages

setup(
    name="fourcats-connector",
    version="0.0.1",
    description="A quick use tool for Python common connectors.",
    packages=find_packages(),
    install_requires=["certifi>=2021.10.8", "loguru>=0.6.0"],
    long_description="""A quick use tool for Python common connectors."""
)
