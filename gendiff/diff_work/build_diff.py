from typing import Any, Final, Union


VALUE_DELETED: Final = 'deleted'
VALUE_ADDED: Final = 'added'
VALUE_CHANGED: Final = 'changed'
VALUE_UNCHANGED: Final = 'unchanged'
VALUE_CHILDREN: Final = 'children'


def build_diff_segment(
        diff_type: str,
        key: str,
        old_value: Any,
        new_value: Any = None,
        children: Union[list, dict] = None
) -> dict:

    return {
        'diff_type': diff_type,
        'key': key,
        'old_value': old_value,
        'new_value': new_value,
        'children': children
    }


def build_diff_segments(
        key: str,
        data1: dict,
        data2: dict
) -> dict:

    if key not in data2:
        data_result = build_diff_segment(
            VALUE_DELETED,
            key,
            data1[key]
        )
    elif key not in data1:
        data_result = build_diff_segment(
            VALUE_ADDED,
            key,
            data2[key]
        )
    elif data1[key] == data2[key]:
        data_result = build_diff_segment(
            VALUE_UNCHANGED,
            key,
            data1[key]
        )
    elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
        data_result = build_diff_segment(
            VALUE_CHILDREN,
            key,
            old_value=None,
            children=build_diff(data1[key], data2[key])
        )
    else:
        data_result = build_diff_segment(
            VALUE_CHANGED,
            key,
            data1[key],
            data2[key]
        )

    return data_result


def build_diff(
        data1: dict,
        data2: dict
) -> list:

    keys = data1.keys() | data2.keys()
    diff = []
    for key in sorted(keys):
        diff.append(build_diff_segments(key, data1, data2))
    return diff
