import json


def json_build(
        diff: list
):
    return json.dumps(diff, indent=4)
