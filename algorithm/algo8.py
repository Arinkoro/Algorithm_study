# -*- coding:utf8 -*-
"""
This is select sort
descending and ascending
"""

import sys

def select_descend(arg_list):
    j = 0
    arg = arg_list
    while(j < len(arg)):
        max = arg[j]
        index = j
        for i in range(j, len(arg)):
            if max < arg[i]:
                max = arg[i]
                index = i
        arg[j], arg[index] = max, arg[j]
        j += 1
    return arg

def select_ascend(arg_list):
    j = 0
    arg = arg_list
    while(j < len(arg)):
        min = arg[j]
        index = j
        for i in range(j, len(arg)):
            if min > arg[i]:
                min = arg[i]
                index = i
        arg[j], arg[index] = min, arg[j]
        j += 1
    return arg

def main():
    args = sys.argv[1:]
    arg = [int(num) for num in args]
    print(select_ascend(arg))



if __name__ == '__main__':
    main()