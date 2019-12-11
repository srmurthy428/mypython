if __name__ == '__main__':
    n = int(input())
    if( n < 2 or n > 10):
        raise Exception('n should not exceed 10 and shouldnt be less than 2: The value of n was: {}'.format(n))
    arr = map(int, input().split())
    len = 0
    lst = []
    for key in arr:
        len += 1
        lst.append(key)
    
    if( n != len):
        raise Exception('the input array shold be of size: {}'.format(n))    
    l = []
    for key in lst:
        if( key < -100 or key > 100):
            raise Exception('array subscript doesnt in range {}',format(key))
        else:
            l.append(key)
    maxInL = max(l)
    while max(l) == maxInL:
        l.remove(maxInL)
    print(max(l))

    