# -*- coding:utf8

def main():
    a = input().split(' ')
    s = ''
    S = list('abcdefghijklmnopqrstuvwxyz')
    for i in range(len(S)):
        s += S[int(a[i]) - 1]
    print(s)
    

if __name__ == '__main__':
    main()