"""
This is algorithm practice
day6 Euclid 
"""
import sys

def main():
    args = sys.argv[1:3]

    m = int(args[0])
    n = int(args[1])
    if m < n:
        tmp = m
        m = n
        n = tmp
    k = m % n
    while(k != 0):
        m = n
        n = k
        k = m % n
    print(n)


if __name__ == '__main__':
    main()