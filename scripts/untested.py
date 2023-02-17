"""
    Coverage report parser
"""
import sys
from pathlib import Path
import os
import re
import argparse
import time # .sleep(), .time(), .time_ns()
import numpy as np

class ColourPrint:

    _HEADER = '\033[95m'
    _OKBLUE = '\033[94m'
    _OKCYAN = '\033[96m'
    _OKGREEN = '\033[92m'
    _WARNING = '\033[93m'
    _FAIL = '\033[91m'
    _ENDC = '\033[0m'
    _BOLD = '\033[1m'
    _UNDERLINE = '\033[4m'

    def __init__(self, col_ok=_OKGREEN, col_fail=_FAIL, col_warn=_WARNING):
        self._ok = col_ok
        self._fail = col_fail
        self._warning = col_warn

    def ok(self, s, file=sys.stdout, end='\n'):
        print(f'{self._ok}{s}{self._ENDC}', end=end, file=file)

    def warning(self, s, file=sys.stdout, end='\n'):
        print(f'{self._warning}{s}{self._ENDC}', end=end, file=file)
    
    def fail(self, s, file=sys.stdout, end='\n'):
        print(f'{self._fail}{s}{self._ENDC}', end=end, file=file)
    
    def bold(self, s, file=sys.stdout, end='\n'):
        print(f'{self._BOLD}{s}{self._ENDC}', end=end, file=file)

    def underline(self, s, file=sys.stdout, end='\n'):
        print(f'{self._UNDERLINE}{s}{self._ENDC}', end=end, file=file)

    def header(self, s, file=sys.stdout, end='\n'):
        print(f'{self._HEADER}{s}{self._ENDC}', end=end, file=file)

parser = argparse.ArgumentParser(
                    prog = 'coverage report parser',
                    description = 'parse output from coverage report',
                    epilog = 'epilog...')
parser.add_argument('path', help='path to report')
parser.add_argument('-u', '--untested', help='show not tested .py files', action='store_true')
parser.add_argument('-t', '--tested', help='show tested .py files', action='store_true')
parser.add_argument('--type', help='path to report', default='branch')
args = parser.parse_args()

def splitter(line, non_empty=True, delim=' '):
    splits = line.split(delim)
    if non_empty:
        splits = list(filter(bool, splits)) 
    return splits

def get_module_details(path):
    if 'algorithms' not in path:
        return None
    files = path.split('/')
    return ([''.join(files[:2])], ''.join(files[2:]))

def make_visited(extension='.py') -> dict:
    """
        Makes a visited dictionary
    """
    tested = {}
    cwd = Path.cwd()
    for file in cwd.glob('**/*' + extension):
        if 'tests' in str(file) or '__init__' in str(file):
            continue
        tested[file.relative_to(cwd)] = False
    return tested

def process(line):
    """
        Processes a line
    """
    data_points = splitter(line)
    path = Path(data_points[0]).cwd()

def parse_lines(lines):
    for line in lines:
        process(line)

def get_untested(lines):
    cwd = Path.cwd()
    files = make_visited()
    for line in lines:
        data = splitter(line)
        if 'algorithms' not in data[0] or 'tests' in data[0]:
            continue
        path = Path(data[0])
        files[path] = True
    return files.items()

def main():
    printer = ColourPrint()
    with open(args.path, 'r') as f:
        lines = f.read().rstrip().split('\n')
        if args.untested or args.tested:
            files = get_untested(lines)
            count = 0
            for (path, tested) in files:
                if tested and args.tested:
                    printer.ok(path)
                elif not tested and args.untested:
                    count += 1
                    printer.fail(path)
            print(f'\n--- {count}, {round(100.0 * count / len(files), 1)}% UNVISITED FILES ---')
            print(f'these have 0.0% code- and branch coverage')
        else:
            output = parse_lines(lines)

if __name__ == "__main__":
    main()
