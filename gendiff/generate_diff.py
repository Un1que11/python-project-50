from gendiff.data_work import file_format, bool_format

import itertools


def generate_diff(file1, file2):
    first_file = file_format(file1)
    second_file = file_format(file2)
    bool_format(first_file)
    bool_format(second_file)
    keys = first_file.keys() | second_file.keys()
    lines = []
    for key in sorted(keys):
        if key not in second_file:
            lines.append(f'  - {key}: {first_file[key]}')
        elif key not in first_file:
            lines.append(f'  + {key}: {second_file[key]}')
        elif first_file[key] == second_file[key]:
            lines.append(f'    {key}: {first_file[key]}')
        else:
            lines.append(f'  - {key}: {first_file[key]}\n  + '
                         f'{key}: {second_file[key]}')
    result = itertools.chain('{', lines, '}')
    return '\n'.join(result)
