from gendiff.diff_work.build_diff import \
    VALUE_ADDED, \
    VALUE_DELETED, \
    VALUE_CHILDREN, \
    VALUE_CHANGED


TEMPLATE_ADDED = "Property '{}' was added with value: {}"
TEMPLATE_REMOVED = "Property '{}' was removed"
TEMPLATE_UPDATED = "Property '{}' was updated. From {} to {}"


def plain(
        diff: list,
        key_list: list = []
) -> str:
    collected_data = list()

    for node in diff:

        diff_type = node['diff_type']
        key = node['key']
        old_value = node['old_value']
        new_value = node['new_value']
        children = node['children']
        key_list.append(key)

        if diff_type == VALUE_DELETED:
            collected_data.append(TEMPLATE_REMOVED.format('.'.join(key_list)))
        elif diff_type == VALUE_ADDED:
            collected_data.append(TEMPLATE_ADDED.format(
                '.'.join(key_list),
                value_format(old_value)))
        elif diff_type == VALUE_CHILDREN:
            collected_data.append(plain(children, key_list))
        elif diff_type == VALUE_CHANGED:
            collected_data.append(TEMPLATE_UPDATED.format(
                '.'.join(key_list),
                value_format(old_value),
                value_format(new_value)))
        key_list.pop()

    return '\n'.join(collected_data)


def value_format(
        value: str
) -> str:
    if isinstance(value, dict):
        value = '[complex value]'
    elif isinstance(value, bool):
        value = str(value).lower()
    elif isinstance(value, str):
        value = f"'{value}'"
    elif value is None:
        value = 'null'
    return value
