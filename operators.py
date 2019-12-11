import sys
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    if( a < 1 or a > 10**10 or b < 1 or b > 10**10):
        sys.exit()
    print(a+b)
    print(a-b)
    print(a*b)