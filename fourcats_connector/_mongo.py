#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# TIME ： 2022-04-12
import json

from loguru import logger

from fourcats_connector._check_requirement import CheckRequirement


class MongoDB:
    """"""

    def __new__(cls, install: bool = False, pip_command: str = "pip", **kwargs):
        """"""
        logger.debug(f"Connecting to mongo server - {json.dumps(kwargs, ensure_ascii=False)}")
        CheckRequirement(check_name="pymongo", install=install, pip_command=pip_command)

        from pymongo import MongoClient
        return MongoClient(**kwargs)
