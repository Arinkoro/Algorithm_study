"""
This is algorithm practice
day 4 time calculate
"""
import sys

def main():
    args = sys.argv
    if len(args) != 7:
        print("input 6 numbers instead of " + str(len(args)))
    else:
        arg = [int(args[i]) for i in range(1, len(args))]
        time1 = arg[0] * 60 * 60 + arg[1] * 60 + arg[2]
        time2 = arg[3] * 60 * 60 + arg[4] * 60 + arg[5]
        sub = time1 - time2
        if sub < 0:
            sub *= -1
        sec = sub % 60
        min = (sub // 60) % 60
        hour = sub / 3600
        print("%d 時間 %d 分 %d 秒\n" %(hour, min, sec))


if __name__ == '__main__':
    main()