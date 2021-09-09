"""
This is algorithm practice
day5 sum number
"""

def main():
    print("Please input 4 numbers")
    sum = 0
    for i in range(4):
        num = int(input())
        sum += num
    print(sum)

if __name__ == "__main__":
    main()