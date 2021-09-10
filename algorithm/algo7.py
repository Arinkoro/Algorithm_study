# -*- coding: utf8 -*-
"""
This is bubble sort cord
ascending order and descending order
"""
import sys

def bubble_ascend(arg_list):
    arg = arg_list
    for i in range(len(arg)):
        if i + 1 < len(arg):
            for j in range(i + 1, len(arg)):
                if arg[i] < arg[j]:
                    arg[i], arg[j] = arg[j], arg[i]
    return arg

def bubble_descend(arg_list):
    arg = arg_list
    for i in range(len(arg)):
        if i + 1 < len(arg):
            for j in range(i + 1, len(arg)):
                if arg[i] > arg[j]:
                    arg[i], arg[j] = arg[j], arg[i]
    return arg_list

def main():
    args = sys.argv[1:]
    arg = [int(num) for num in args]
    answer = bubble_descend(arg)
    print(answer)

            
        

if __name__ == '__main__':
    main()