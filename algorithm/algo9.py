# -*- coding: utf-8 -*-
"""
This code is insert sort
ascending and descending
"""
import sys

def insert_descend(arg):
    if arg[0] < arg[1]:
        arg[0], arg[1] = arg[1], arg[0]
    for i in range(2, len(arg)):
        for j in range(i):
            if arg[j] < arg[i]:
                arg.insert(j, arg[i])
                arg.pop(i + 1)
                break
    return arg

def insert_ascend(arg):
    if arg[0] > arg[1]:
        arg[0], arg[1] = arg[1], arg[0]
    for i in range(2, len(arg)):
        for j in range(i):
            if arg[j] > arg[i]:
                arg.insert(j, arg[i])
                arg.pop(i + 1)
                break
    return arg


def main():
    args = sys.argv[1:]
    arg = [int(num) for num in args]
    print(insert_ascend(arg))



if __name__ == '__main__':
    main()