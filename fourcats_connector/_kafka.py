#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# TIME ： 2022-04-12
import json

from loguru import logger

from fourcats_connector._check_requirement import CheckRequirement


class Kafka:
    """"""

    def __init__(self, install: bool = False, pip_command: str = "pip", **kwargs):
        """"""
        CheckRequirement(check_name="kafka", package_name="kafka-python", install=install, pip_command=pip_command)
        self.__configs = kwargs
        self.producer = self.__producer()

    def __producer(self):
        """"""
        from kafka import KafkaProducer
        configs = {key: value for key, value in self.__configs.items() if key in KafkaProducer.DEFAULT_CONFIG.keys()}
        logger.debug(f"正在连接 Kafka 生产者服务器 - {json.dumps(configs, ensure_ascii=False)}")
        return KafkaProducer(**configs)

    def consumer(self, *topics: str):
        """"""
        from kafka import KafkaConsumer
        configs = {key: value for key, value in self.__configs.items() if key in KafkaConsumer.DEFAULT_CONFIG.keys()}
        logger.debug(f"Connecting to kafka consumer server - {json.dumps(configs, ensure_ascii=False)}, "
                     f"Topics - {json.dumps(topics, ensure_ascii=False)}")
        return KafkaConsumer(*topics, **configs)
