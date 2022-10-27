from gendiff.generate_diff import generate_diff


def test_gendiff_json():
    with open('tests/fixtures/json_result.txt') as file:
        expected = file.read()

    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')\
           == expected


def test_gendiff_yaml():
    with open('tests/fixtures/yml_result.txt') as file:
        expected = file.read()

    assert generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml')\
           == expected


def test_format_stylish_json():
    with open('tests/fixtures/stylish_result.txt') as file:
        expected = file.read()

    assert generate_diff('tests/fixtures/file1_tree.json',
                         'tests/fixtures/file2_tree.json')\
           == expected


def test_format_stylish_yml():
    with open('tests/fixtures/stylish_result.txt') as file:
        expected = file.read()

    assert generate_diff('tests/fixtures/file1_tree.yml',
                         'tests/fixtures/file2_tree.yml')\
           == expected


def test_format_plain_json():
    with open('tests/fixtures/plain_result.txt') as file:
        expected = file.read()

    assert generate_diff('tests/fixtures/file1_tree.json',
                         'tests/fixtures/file2_tree.json',
                         style='plain')\
           == expected


def test_format_plain_yml():
    with open('tests/fixtures/plain_result.txt') as file:
        expected = file.read()

    assert generate_diff('tests/fixtures/file1_tree.yml',
                         'tests/fixtures/file2_tree.yml',
                         style='plain') \
           == expected


def test_format_json():
    with open('tests/fixtures/format_json_result.txt') as file:
        expected = file.read()

    assert generate_diff('tests/fixtures/file1_tree.json',
                         'tests/fixtures/file2_tree.json',
                         style='json')\
           == expected
