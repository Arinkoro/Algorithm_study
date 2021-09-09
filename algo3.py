"""
This is algorithm practice
day 5 max number
"""
import sys

def main():
    args = sys.argv
    max = 0
    if len(args) != 5:
        print("input 4 numbers instead of {}".format(len(args)))
    else:
        arg = [int(args[i]) for i in range(1, len(args))]
        for num in arg:
            if num > max:
                max = num
        print(max)
if __name__ == '__main__':
    main()