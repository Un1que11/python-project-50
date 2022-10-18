from gendiff.generate_diff import generate_diff
from gendiff.scripts.gendiff import main


def test_gendiff_json():
    with open('tests/fixtures/json_result') as file:
        expected = file.read()

    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')\
           == expected


def test_gendiff_yaml():
    with open('tests/fixtures/yml_result') as file:
        expected = file.read()

    assert generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml')\
           == expected


def test_gendiff_tree_json():
    with open('tests/fixtures/json_tree_result') as file:
        expected = file.read()

    assert generate_diff('tests/fixtures/file1_tree.json',
                         'tests/fixtures/file2_tree.json')\
           == expected


def test_gendiff_tree_yml():
    with open('tests/fixtures/yml_tree_result') as file:
        expected = file.read()

    assert generate_diff('tests/fixtures/file1_tree.yml',
                         'tests/fixtures/file2_tree.yml')\
           == expected
