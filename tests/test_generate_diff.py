import pytest
from gendiff.diff_work.generate_diff import generate_diff


def open_file(file_path):
    with open(file_path) as file:
        expected = file.read()
    return expected


@pytest.mark.parametrize(
    'file_path1, file_path2, test_format, result_path', [
        (
            'tests/fixtures/file1.json',
            'tests/fixtures/file2.json',
            'stylish',
            'tests/fixtures/json_result.txt'
        ),
        (
            'tests/fixtures/file1.yml',
            'tests/fixtures/file2.yml',
            'stylish',
            'tests/fixtures/yml_result.txt'
        ),
        (
            'tests/fixtures/file1_tree.json',
            'tests/fixtures/file2_tree.json',
            'stylish',
            'tests/fixtures/stylish_result.txt'
        ),
        (
            'tests/fixtures/file1_tree.yml',
            'tests/fixtures/file2_tree.yml',
            'stylish',
            'tests/fixtures/stylish_result.txt'
        ),
        (
            'tests/fixtures/file1_tree.json',
            'tests/fixtures/file2_tree.json',
            'plain',
            'tests/fixtures/plain_result.txt'
        ),
        (
            'tests/fixtures/file1_tree.yml',
            'tests/fixtures/file2_tree.yml',
            'plain',
            'tests/fixtures/plain_result.txt'
        ),
        (
            'tests/fixtures/file1_tree.json',
            'tests/fixtures/file2_tree.json',
            'json',
            'tests/fixtures/format_json_result.txt'
        ),
    ],
)
def test_generate_diff(file_path1, file_path2, test_format, result_path):
    expected = open_file(result_path)
    test_diff = generate_diff(file_path1, file_path2, test_format)

    assert test_diff == expected
