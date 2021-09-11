# -*- coding:utf8

def has_duplicates2(seq):
    seen = []
    unique_list = [x for x in seq if x not in seen and not seen.append(x)]
    return len(seq) != len(unique_list)

def main():
    N = int(input())
    X_list = []
    y_list = []
    for i in range(N):
        pivot = input().split(" ")
        x, y = int(pivot[0]), int(pivot[1])
        X_list.append([x, y])
        y_list.append(x)
    sort_list = sorted(X_list)
    sort_x_list = sorted(y_list)
    dup = [x for x in set(sort_x_list) if sort_x_list.count(x) > 1]
    print(sort_list)
    print(dup)
    


        

if __name__ == '__main__':
    main()