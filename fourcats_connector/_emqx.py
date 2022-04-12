#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# TIME ： 2022-04-12
import json

from loguru import logger

from fourcats_connector._check_requirement import CheckRequirement


class Emqx:
    """"""

    def __new__(cls, install: bool = False, pip_command: str = "pip", **kwargs):
        logger.debug(f"Connecting to emqx server - {json.dumps(kwargs, ensure_ascii=False)}")

        CheckRequirement(check_name="paho", package_name="paho-mqtt", install=install, pip_command=pip_command)
        import paho.mqtt.client as mqtt

        client_fields = ["client_id", "clean_session", "userdata", "protocol", "transport", "reconnect_on_failure"]
        auth_fields = ["username", "password"]
        connect_fields = ["host", "port", "keepalive", "bind_address", "bind_port", "clean_start", "properties"]

        mqtt_server = mqtt.Client(**{key: value for key, value in kwargs.items() if key in client_fields})

        mqtt_server.username_pw_set(**{key: value for key, value in kwargs.items() if key in auth_fields})

        mqtt_server.connect(**{key: value for key, value in kwargs.items() if key in connect_fields})
        mqtt_server.loop_start()
        return mqtt_server
