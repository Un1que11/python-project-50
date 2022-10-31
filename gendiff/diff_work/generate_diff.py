from gendiff.formatters.style_format import style_format
from gendiff.diff_work.data_work import get_file_data_and_format
from gendiff.diff_work.build_diff import build_diff
from gendiff.diff_work.parser import parse


def generate_diff(
        file1: str,
        file2: str,
        style='stylish'
) -> str:

    file1_data, file1_format = get_file_data_and_format(file1)
    file2_data, file2_format = get_file_data_and_format(file2)

    file1_parse = parse(file1_data, file1_format)
    file2_parse = parse(file2_data, file2_format)

    diff = build_diff(file1_parse, file2_parse)
    return style_format(diff, style)
