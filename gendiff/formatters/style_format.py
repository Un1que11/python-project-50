from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import json_build


def style_format(
        diff: list,
        style: str
) -> str:
    if style == 'stylish':
        return stylish(diff)
    elif style == 'json':
        return json_build(diff)
    else:
        return plain(diff)
