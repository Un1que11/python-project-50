from gendiff.formatters.style_format import style_format
from gendiff.diff_work.data_work import open_file
from gendiff.diff_work.build_diff import build_diff


def generate_diff(
        file1: str,
        file2: str,
        style='stylish'
) -> str:

    first_file = open_file(file1)
    second_file = open_file(file2)
    diff = build_diff(first_file, second_file)
    return style_format(diff, style)
