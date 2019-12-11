def supplementRow(midStr,column):
    suppl = column - len(midStr)
    if(suppl % 2 != 0):
        raise Exception('supplemental columns should be even')
    for i in range(0, round(suppl/2)):
        midStr = '-' + midStr
        i += 1
    
    for i in range(0, round(suppl/2)):
        midStr = midStr + '-'
        i += 1
    return midStr

if __name__ == '__main__':
    rowS, columnS = input().split()
    row = int(rowS)
    column = int(columnS)
    if(row < 5 or row > 101 or row % 2 == 0 or row * 3 != column):
        raise Exception("row should be an odd number between 5 and 101 and column should be 3 times of row ")
    rowstr = ''
    midStr =''
    midstr_dict = {}
    rrow = row + 1
    midNo =  round(rrow/2)
    
    for i in range(1,rrow):
        rowstr = ''
        if ( i < midNo):
            if(midStr == ''):
                midStr ='.|.'
                midstr_dict[i] = midStr
            else:
                midStr = midStr +'.|.'+'.|.' 
                midstr_dict[i] = midStr
        elif ( i == midNo):
                midStr ='WELCOME'
                midstr_dict[i] = midStr
        elif ( i > midNo):
               x = i % midNo
               midStr = midstr_dict[midNo-x]
        print(supplementRow(midStr,column))
        #print(j)
    i += 1
             