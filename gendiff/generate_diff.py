import json
import itertools


def generate_diff(file1, file2):
    first_file = json.load(open(f'{file1}'))
    second_file = json.load(open(f'{file2}'))
    lines = []
    for key, value in sorted(first_file.items()):
        if key in second_file and first_file[key] == second_file[key]:
            lines.append(f'    {key}: {value}')
        elif key in second_file and first_file[key] != second_file[key]:
            lines.append(f'  - {key}: {value}\n  + {key}: {second_file[key]}')
        elif key not in second_file:
            lines.append(f'  - {key}: {value}')
    for key, value in sorted(second_file.items()):
        if key not in first_file:
            lines.append(f'  + {key}: {value}')
    result = itertools.chain('{', lines, '}')
    return '\n'.join(result)
