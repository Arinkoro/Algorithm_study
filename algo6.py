"""
This code is algorithm practice
day7 soinsubunkai
"""

import sys
import math

def elatnes(num):
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
    return answer

def main():
    m = int(sys.argv[1])
    n = m - 1

    while(m % n != 0):
        n -= 1
    d = m / n
    answer = []
    answer.append(d)
    while(m not in elatnes(m)):
        m = n // d
        answer.append(d)
    answer.append(m)
    print(answer)






if __name__ == '__main__':
    main()