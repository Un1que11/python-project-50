from pathlib import Path

import json
import yaml


def file_format(file):
    if Path(file).suffix == '.json':
        with open(f'{file}') as f:
            return json.load(f)

    elif Path(file).suffix == '.yml' or Path(file).suffix == '.yaml':
        with open(f'{file}') as f:
            return yaml.safe_load(f)


def bool_format(dictionary):
    for key in dictionary:
        if dictionary[key] is False:
            dictionary[key] = 'false'
        elif dictionary[key] is True:
            dictionary[key] = 'true'
