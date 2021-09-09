"""
This is algorithm practice
day 6 eratstnes
"""
import sys
import math

def main():
    num = int(sys.argv[1])
    args = [i for i in range(1, num + 1)]
    if 1 in args:
        args[0] = 0
    pivot = math.sqrt(num)
    for i in range(1, len(args)):
        if args[i] % 2 == 0 and args[i] != 2:
            args[i] = 0
    num = 3
    while(num < pivot):
        for i in range(2, len(args)):
            if args[i] != 0:
                if args[i] % num == 0 and args[i] != num:
                    args[i] = 0
        num += 2
    answer = [i for i in args if i != 0]
    print(answer)
    print("素数の数 {}".format(len(answer)))


if __name__ == '__main__':
    main()