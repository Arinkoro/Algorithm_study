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
    d = int(m / n)
    answer = []
    answer.append(d)
    while(n not in elatnes(m)):
        if n % d == 0:
            n = int(n / d)
        else:
            m = n
            n = m - 1
            while(m % n != 0):
                n -= 1
                d = int(m / n)

        answer.append(d)
    answer.append(n)
    print(answer)






if __name__ == '__main__':
    main()