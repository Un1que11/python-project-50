import json

import yaml


def parse(
        file_data: str,
        file_format: str
) -> dict:
    if file_format == 'json':
        return json.loads(file_data)
    return yaml.safe_load(file_data)
