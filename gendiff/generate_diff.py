import json
import itertools


def bool_format(dictionary):
    for key in dictionary:
        if dictionary[key] is False:
            dictionary[key] = 'false'
        elif dictionary[key] is True:
            dictionary[key] = 'true'


def generate_diff(file1, file2):
    first_file = json.load(open(f'{file1}'))
    second_file = json.load(open(f'{file2}'))
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
