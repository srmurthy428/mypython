class CmdLst:
    def __init__(self,cmd,lst):
        self.cmd = cmd
        self.lst = lst
    def __repr__(self):
        return "CmdLst({0},{1})".format(self._cmd,self._lst)
    def __str__(self):
        return "CmdLst({0},{1})".format(self._cmd,self._lst)

    @property
    def cmd(self):
        return self._cmd

    @property
    def lst(self):
        return self._lst

    @cmd.setter
    def cmd(self, value):
        self._cmd = value

    @lst.setter
    def lst(self, value):
        self._lst = value

if __name__ == '__main__':
    fullList = []
    c = CmdLst('insert',[1,2,3])
    print(c)
    fullList.append(c)
    c = CmdLst('append',[4])
    fullList.append(c)
    c = CmdLst('insert',[5,6,7])
    fullList.append(c)
    c = CmdLst('remove',[1])
    fullList.append(c)
    print(fullList)
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    for x in fullList:
        print(x.cmd, end='')
        print(x.lst)
    print('dssdsds')
    listx = [5, 8, 2, 1, 8,3]
    listx.reverse()
    print(listx)
    listx.pop()
    print(listx)
    listx.sort()
    print(listx)
