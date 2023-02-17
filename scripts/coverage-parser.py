"""
    Parse branch coverage
"""
import sys
import os
import re
import argparse
import time # .sleep(), .time(), .time_ns()
import numpy as np

parser = argparse.ArgumentParser(
                    prog = 'collide parsing',
                    description = 'add all together',
                    epilog = 'of the parsing')
parser.add_argument('path', help='input path/file')
args = parser.parse_args()

def main():
    with open(args.path, 'r') as f:
        lines = f.read().rstrip().split('\n')
        functions = dict()
        i = 0
        for line in lines:
            if i < 2:
                i += 1
                continue
            spl = line.split(',')
            name = spl[0]
            inititalised = False
            if name not in functions:
                inititalised = True
                functions[name] = set()
            if float(spl[2]) > 0.99999:
                # full coverage
                continue
            not_covered = spl[3].split(';')
            if inititalised:
                for branch in not_covered:
                    functions[name].add(branch)
            else:
                to_remove = []
                for branch in functions[name]:
                    if branch not in not_covered:
                        to_remove.append(branch)

                for branch in to_remove:
                    functions[name].remove(branch)
        for (name, branches) in functions.items():
            print(f'{name} : {branches if len(branches) > 0 else None}')







if __name__ == "__main__":
    main()
