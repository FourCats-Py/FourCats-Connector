#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# TIME ： 2022-04-12
import os

from loguru import logger


class CheckRequirement:

    def __init__(self, check_name: str, package_name: str = None, version: str = None, install: bool = False,
                 pip_command: str = "pip"):
        """"""
        if package_name is None:
            package_name = check_name

        self.__check(
            check_name=check_name, package_name=package_name, version=version, install=install, pip_command=pip_command
        )

    @staticmethod
    def __check(check_name, package_name, version, install, pip_command):
        """"""
        try:
            exec("import {0}".format(check_name))
        except ModuleNotFoundError as e:
            logger.warning("This script requires {}.".format(package_name))
            if install is True:
                _command = package_name
                if version is not None and isinstance(version, str):
                    if "=" in version or ">" in version or "<" in version or "~" in version:
                        _command = "'" + package_name + version + "'"
                    else:
                        _command = package_name + "==" + version
                logger.info("Execute commands: {}".format(" ".join([pip_command, "install", _command])))
                os.system(" ".join([pip_command, "install", _command]))
                return
            raise e
