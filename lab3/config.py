#!/bin/python3

import json


CONFIG_FILE_NAME = "lab3/config.json"


def _get_dict(file_name):
    with open(file_name) as json_file:
        return json.load(json_file)


configuration = _get_dict(CONFIG_FILE_NAME)
ROUTER_NUMBER = configuration["routers_number"]
DISTANCE = configuration["distance"]
DISTANCE_2 = DISTANCE * DISTANCE
MAX_VELOCITY = configuration["max_velocity"]
WINDOW_SIZE = configuration["window_size"]
PACKAGE = configuration["package"]
TIMEOUT = configuration["timeout"]
