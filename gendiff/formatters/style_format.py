from gendiff.formatters.stylish import run_stylish
from gendiff.formatters.plain import run_plain
from gendiff.formatters.json import json_build


def style_format(
        diff: list,
        style: str
) -> str:
    if style == 'stylish':
        return run_stylish(diff)
    elif style == 'json':
        return json_build(diff)
    else:
        return run_plain(diff)
