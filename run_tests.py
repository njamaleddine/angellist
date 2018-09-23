#! /usr/bin/env python
import subprocess
import sys


def run_tests(args=['--cov=angellist', 'tests/', '--verbose']):
    print('Running tests with pytest...')
    return subprocess.call(['pytest'] + args)


def run_linter():
    print('Linting with flake8...')
    result = subprocess.call(['flake8', 'angellist'])
    if not result:
        print('No issues found by flake8')
    return result


if __name__ == '__main__':
    commands = (
        run_linter,
        run_tests,
    )

    for command in commands:
        result = command()
        if result:
            sys.exit(result)
