from gendiff.formatters.stylish import stylish
from gendiff.diff_work.data_work import open_file


def generate_diff(
        file1: str,
        file2: str,
        style=stylish) -> str:
    first_file = open_file(file1)
    second_file = open_file(file2)
    return style(first_file, second_file)
