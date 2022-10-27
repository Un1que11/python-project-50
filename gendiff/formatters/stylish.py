from itertools import chain
from gendiff.diff_work.data_work import bool_format, null_format
from gendiff.diff_work.build_diff import \
    VALUE_UNCHANGED, \
    VALUE_ADDED, \
    VALUE_DELETED, \
    VALUE_CHILDREN


def stylish(diff, depth=1):
    collected_data = list()
    spaces = 4 * depth - 2
    indent = ' ' * spaces

    for node in diff:
        bool_format(node)
        null_format(node)

        diff_type = node['diff_type']
        key = node['key']
        old_value = node['old_value']
        new_value = node['new_value']
        children = node['children']

        if diff_type == VALUE_DELETED:
            collected_data.append(f'{indent}- {key}: '
                                  f'{value_format(old_value, depth + 1)}')
        elif diff_type == VALUE_ADDED:
            collected_data.append(f'{indent}+ {key}: '
                                  f'{value_format(old_value, depth + 1)}')
        elif diff_type == VALUE_UNCHANGED:
            collected_data.append(f'{indent}  {key}: '
                                  f'{value_format(old_value, depth + 1)}')
        elif diff_type == VALUE_CHILDREN:
            collected_data.append(f'{indent}  {key}: '
                                  f'{stylish(children, depth + 1)}')
        else:
            collected_data.append(f'{indent}- {key}: '
                                  f'{value_format(old_value, depth + 1)}\n'
                                  f'{indent}+ {key}: '
                                  f'{value_format(new_value, depth + 1)}')
    result = chain('{', collected_data, [' ' * (spaces - 2) + '}'])
    return '\n'.join(result)


def value_format(value, depth):
    collected_data = list()
    spaces = 4 * depth - 2
    indent = ' ' * spaces

    if isinstance(value, dict):
        for key, dict_value in value.items():
            collected_data.append(f'{indent}  {key}: '
                                  f'{value_format(dict_value, depth + 1)}')
    elif isinstance(value, bool):
        collected_data.append(str(value).lower())
    elif value is None:
        collected_data.append('null')
    else:
        return str(value)

    result = chain('{', collected_data, [' ' * (spaces - 2) + '}'])
    return '\n'.join(result)
