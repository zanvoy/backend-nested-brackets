#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "Mike Gabbard in colaboration with Ybrayym Abamov"

import sys


def is_nested(line):
    """Validate a single input line for correct nesting"""
    valid = []
    tokens_dict = {')': '(',
        ']': '[',
        '}': '{',
        '>': '<',
        '*)': '(*'
        }
    count = 0
    for index, char in enumerate(line):
        if char == '(' and index != len(line)-1 and line[index+1] == '*':
            count += 1
            valid.append('(*')
        elif char == ')' and index-2 >= 0 and line[index - 1] == '*' and line[index-2] != '(':
            count += 1
            if valid[-1] == '(*':
                valid.pop()
            else:
                return 'NO ' + str(index+1-count)
        else:
            if char in tokens_dict.values():
                valid.append(char)
            if char in tokens_dict.keys():
                if tokens_dict[char] == valid[-1]:
                    valid.pop()
                else:
                    return 'NO ' + str(index + 1-count)
    if valid == []:
        return 'YES'
    else:
        return 'NO ' + str(len(line)-count)

def main(args):
    """Open the input file and call `is_nested()` for each line"""
    # Results: print to console and also write to output file
    with open(args[0]) as file:
        for line in file:
            print(is_nested(line))
            f = open("output.txt", "a")
            f.write(is_nested(line)+ '\n')

if __name__ == '__main__':
    main(sys.argv[1:])
