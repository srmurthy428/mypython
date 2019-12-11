""" if __name__ == '__main__':
    n = int(input())
    x=0
    for x in range(n):
        print(x)
        print(x**2) """

def is_leap(year):
    leap = False
    if( year < 1900 or year > 10**5):
        leap = False
    elif( year % 4 ==0 ):
        leap = True 
    return leap

year = int(input())
print(is_leap(year))