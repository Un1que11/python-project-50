#!/usr/bin/env python3
from gendiff.cli.cli import parse_cli_arguments
from gendiff.diff_work.generate_diff import generate_diff


def main():
    first_file, second_file, style = parse_cli_arguments()

    print(generate_diff(first_file, second_file, style))


if __name__ == '__main__':
    main()
