from pathlib import Path


def get_data_file(
        file: str
) -> str:
    with open(f'{file}', 'r') as file_data:
        return file_data.read()


def get_file_format(
        file: str
) -> str:
    if Path(file).suffix == '.yml' or Path(file).suffix == '.yaml':
        return 'yml'
    elif Path(file).suffix == '.json':
        return 'json'


def get_file_data_and_format(
    file: str
) -> tuple:
    file_data = get_data_file(file)
    file_format = get_file_format(file)
    return file_data, file_format


def bool_format(
        dictionary: dict
):
    for key in dictionary:
        if dictionary[key] is False:
            dictionary[key] = 'false'
        elif dictionary[key] is True:
            dictionary[key] = 'true'


def null_format(
        dictionary: dict
):
    for key in dictionary:
        if dictionary[key] is None:
            dictionary[key] = 'null'
