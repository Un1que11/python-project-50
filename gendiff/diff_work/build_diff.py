from typing import Any, Final, Union


VALUE_DELETED: Final = 'deleted'  # key in first, but no in second
VALUE_ADDED: Final = 'added'  # key in second, but no in first
VALUE_CHANGED: Final = 'changed'  # key in first and second, but values different
VALUE_UNCHANGED: Final = 'unchanged'  # key in first and second and values are the same
VALUE_CHILDREN: Final = 'children'


def create_diff_segment(
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


def create_diff_segments(
        key: str,
        file1: dict,
        file2: dict
) -> dict:

    if key not in file2:
        data_result = create_diff_segment(
            VALUE_DELETED,
            key,
            file1[key]
        )
    elif key not in file1:
        data_result = create_diff_segment(
            VALUE_ADDED,
            key,
            file2[key]
        )
    elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
        data_result = create_diff_segment(
            VALUE_CHILDREN,
            key,
            old_value=None,
            children=create_diff(
                file1[key],
                file2[key]
            )
        )
    elif file1[key] == file2[key]:
        data_result = create_diff_segment(
            VALUE_UNCHANGED,
            key,
            file1[key]
        )
    else:
        data_result = create_diff_segment(
            VALUE_CHANGED,
            key,
            file1[key],
            file2[key]
        )

    return data_result


def create_diff(
        file1: dict,
        file2: dict
) -> list:

    keys = file1.keys() | file2.keys()
    diff = []
    for key in sorted(keys):
        diff.append(create_diff_segments(key, file1, file2))
    return diff
