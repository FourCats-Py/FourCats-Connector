#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# TIME ： 2022-04-12
import json

from loguru import logger

from fourcats_connector._check_requirement import CheckRequirement


class Redis:
    """"""

    def __new__(cls, install: bool = False, pip_command: str = "pip", **kwargs):
        """"""
        logger.debug(f"Connecting to redis server - {json.dumps(kwargs, ensure_ascii=False)}")
        CheckRequirement(check_name="redis", install=install, pip_command=pip_command)
        if "startup_nodes" in kwargs:
            return cls.cluster(install, pip_command, **kwargs)
        elif "sentinel_nodes" in kwargs:
            return cls.sentinel(**kwargs)
        else:
            return cls.standalone(**kwargs)

    @classmethod
    def standalone(cls, **kwargs):
        """Connect stand-alone"""
        import redis

        if "decode_responses" not in kwargs:
            kwargs["decode_responses"] = True
        pool = redis.ConnectionPool(**kwargs)
        return redis.Redis(connection_pool=pool)

    @classmethod
    def cluster(cls, install, pip_command, **kwargs):
        """Connect cluster"""
        CheckRequirement(
            check_name="rediscluster", package_name="redis-py-cluster", install=install, pip_command=pip_command
        )

        from rediscluster import ClusterConnectionPool, RedisCluster

        if "decode_responses" not in kwargs:
            kwargs["decode_responses"] = True
        pool = ClusterConnectionPool(**kwargs)
        return RedisCluster(connection_pool=pool)

    @classmethod
    def sentinel(cls, sentinel_nodes, master_node=None, slave_node=None, **kwargs):
        """"Connect sentinel"""
        import redis.sentinel

        class Sentinel(redis.sentinel.Sentinel):
            pass

        sentinels = [(sentinel_node["host"], sentinel_node["port"]) for sentinel_node in sentinel_nodes]
        obj = Sentinel(sentinels=sentinels, **kwargs)

        if master_node is not None and isinstance(master_node, dict):
            if "decode_responses" not in master_node:
                master_node["decode_responses"] = True
            setattr(obj, "master_node", obj.master_for(**master_node))

        if slave_node is not None and isinstance(slave_node, dict):
            if "decode_responses" not in slave_node:
                slave_node["decode_responses"] = True
            setattr(obj, "slave_node", obj.master_for(**slave_node))

        return obj
