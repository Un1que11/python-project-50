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
        file1: dict,
        file2: dict
) -> dict:

    if key not in file2:
        data_result = build_diff_segment(
            VALUE_DELETED,
            key,
            file1[key]
        )
    elif key not in file1:
        data_result = build_diff_segment(
            VALUE_ADDED,
            key,
            file2[key]
        )
    elif file1[key] == file2[key]:
        data_result = build_diff_segment(
            VALUE_UNCHANGED,
            key,
            file1[key]
        )
    elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
        data_result = build_diff_segment(
            VALUE_CHILDREN,
            key,
            old_value=None,
            children=build_diff(
                file1[key],
                file2[key]
            )
        )
    else:
        data_result = build_diff_segment(
            VALUE_CHANGED,
            key,
            file1[key],
            file2[key]
        )

    return data_result


def build_diff(
        file1: dict,
        file2: dict
) -> list:

    keys = file1.keys() | file2.keys()
    diff = []
    for key in sorted(keys):
        diff.append(build_diff_segments(key, file1, file2))
    return diff
