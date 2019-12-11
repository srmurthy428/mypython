if __name__ == '__main__':
    S = input()
    if ( S.isalnum()== False):
        raise Exception("S is not alphanumeric")
    listS = list(S)
    upperCaseList=[]
    lowerCaseList=[]
    oddDigitList=[]
    evenDigitList=[]

    print(listS)
    for x in listS:
        if(x.isupper()):
            upperCaseList.append(x)
        elif (x.islower()):
            lowerCaseList.append(x)
        elif(x.isnumeric()):
            if(int(x) % 2 == 0):
                evenDigitList.append(int(x))
            else:
                oddDigitList.append(int(x))
    upperCaseList.sort()
    lowerCaseList.sort()
    oddDigitList.sort()
    evenDigitList.sort()
    lowerCaseList.extend(upperCaseList)
    lowerCaseList.extend(oddDigitList)
    lowerCaseList.extend(evenDigitList)
    for x in lowerCaseList:
        print(x,end='')