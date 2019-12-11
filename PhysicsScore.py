def takeSecond(elem):
    return elem[1]
def takeFirst(elem):
    return elem[0]    
def lowMarkk(elem):
     return elem[0][1]   
if __name__ == '__main__':
    fullList=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l = list((name,score))
        fullList.append(l)
    fullList.sort(key=takeSecond)
    lowMark = 0.00
    if len(fullList) > 0:
        lowMark = lowMarkk(fullList)
    newList=[]
    for inner_l in fullList:
        if( float(inner_l[1]) > lowMark) :
            newList.append(inner_l)
    newList.sort(key=takeSecond)
  

    if len(newList) > 0:
        lowMark = lowMarkk(newList)
    newnewList=[]
    for inner_l in newList:
        if( float(inner_l[1]) == lowMark):
            newnewList.append(inner_l)
    newnewList.sort(key=takeFirst)
    for inner_l in newnewList:
        print(inner_l[0])



