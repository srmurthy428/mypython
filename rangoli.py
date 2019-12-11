def makeRow(lst,cntr):
    row=''
    for i in range(0,cntr):
        row = row + "-"
    row = list(row)
    i=0
    doubleLen = len(lst) * 2
    doubleLen = int(doubleLen)
    previ = 0
    while( i < doubleLen) :
        if (i== 0):
            row[i] = lst[i]
        else: 
            previ = previ + 2
            if ( i + 1 <= len(lst) ):
                row[previ] = lst[i]
        i += 1
    return row

def makeString(lst):
    str =''
    for x in lst:
        str = str + x
    return str
def print_rangoli(size):
    numrows = (size * 2) - 1
    columnsize = (size * 4) - 3
    lst = list('abcdefghijklmnopqrstuvwxyz')
    sublst = lst[0:size]
    rangoli_dict = {}
    if( len(sublst) != size):
        raise Exception ("size doesn't match")
    i = size
         
    cntr = int((columnsize + 1)/2)
    j = 0
    while i > 0:
        halfrow = makeRow(sublst[j:size],cntr) 
        halfrowStr= makeString(halfrow)
        halfrow.reverse()
        alfrowStr= makeString(halfrow)
        if (len(alfrowStr) > 0 and alfrowStr[len(alfrowStr)-1] != '-') :
            concatrow = alfrowStr[0:len(alfrowStr)-1]+halfrowStr
            if (len(concatrow)==columnsize):
                rangoli_dict[i] = concatrow
            else:
                print('MISMATCH')
            j += 1    
            i -= 1
    i = 1
    while i <= size:
        print(rangoli_dict[i])
        i += 1
    i = size - 1
    while i > 0:
        print(rangoli_dict[i])
        i -= 1
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)