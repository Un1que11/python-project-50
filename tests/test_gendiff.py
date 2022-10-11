from gendiff.generate_diff import generate_diff


def test_gendiff_json():
    with open('tests/fixtures/json_result') as file:
        expected = file.read()

    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')\
           == expected
