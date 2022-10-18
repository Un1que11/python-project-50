from gendiff.scripts.gendiff import main

import os
import pytest


def test_help_command():
    exit_status = os.system('gendiff -h')
    assert exit_status == 0


def test_cli_without_arg():
    with pytest.raises(SystemExit):
        main()
        pytest.fail()
