#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# TIME ： 2022-04-12
import json

from loguru import logger

from fourcats_connector._check_requirement import CheckRequirement


class MySQL:
    """"""

    def __new__(cls, install: bool = False, pip_command: str = "pip", **kwargs):
        """"""
        logger.debug(f"Connecting to mysql server - {json.dumps(kwargs, ensure_ascii=False)}")
        CheckRequirement(check_name="pymysql", install=install, pip_command=pip_command)
        CheckRequirement(check_name="dbutils", version=">=3.0.0", install=install, pip_command=pip_command)

        import pymysql
        from dbutils.pooled_db import PooledDB
        return PooledDB(creator=pymysql, cursorclass=pymysql.cursors.DictCursor, **kwargs)
