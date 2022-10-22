### Hexlet tests and linter status:
[![Actions Status](https://github.com/Un1que11/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/Un1que11/python-project-50/actions)
[![Build Status](https://github.com/Un1que11/python-project-50/actions/workflows/project-check.yml/badge.svg)](https://github.com/Un1que11/python-project-50/actions/workflows/project-check.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/c6148e823b09f10e7d49/maintainability)](https://codeclimate.com/github/Un1que11/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/c6148e823b09f10e7d49/test_coverage)](https://codeclimate.com/github/Un1que11/python-project-50/test_coverage)

# Gendiff
## Description:
CLI utilite that shows difference between two JSON or YML files
## Dependencies:

* python = "^3.10"
* pytest = "^7.1.3"
* PyYAML = "^6.0"
## Usage:
    usage: gendiff [-h] [-f FORMAT] first_file second_file

    Generate diff

    positional arguments:
      first_file
      second_file

    optional arguments:
      -h, --help            show help message and exit
      -f, --format          set format of output
## Installation:
### Use the package manager pip:
    pip install --user git+https://github.com/Un1que11/python-project-50.git
### or 
### Clone repository and use poetry:
    git clone https://github.com/Un1que11/python-project-50.git
    cd python-project-50
    make build
    make reinstall
## Work process:

+ gendiff (file.json):

      gendiff first_file.json second_file.json
[![asciicast](https://asciinema.org/a/ECfGIFIaGenyvY6s8ksXL1lnq.svg)](https://asciinema.org/a/ECfGIFIaGenyvY6s8ksXL1lnq)

+ gendiff (file.yml)

      gendiff first_file.yml second_file.yml
[![asciicast](https://asciinema.org/a/JGSPTyWj8fRAA3RYg9BtDC6ZV.svg)](https://asciinema.org/a/JGSPTyWj8fRAA3RYg9BtDC6ZV)