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
    n = int(input())
    full_list = []
    my_list=[]
    for _ in range(n):
        cmd, *line = input().split()
        mmbrs = list(map(int, line))
        l = CmdLst(cmd,mmbrs)
        full_list.append(l)
    
    for x in full_list:
        cmd = x.cmd
        lst = x.lst
        if(cmd == 'insert'): 
            if (len(lst) < 2):
                raise Exception("Insert command needs two arguments")
            elif (len(lst) == 2):
                my_list.insert(lst[0],lst[1])
        elif ( cmd == 'append'):
            if (len(lst) != 1):
                raise Exception("append command just one argument")
            elif (len(lst) == 1):
                my_list.extend(lst)
        elif ( cmd == 'remove'):
            if (len(lst) > 0):
                my_list.remove(lst[0])
        elif ( cmd == 'pop'):
            my_list.pop()
        elif ( cmd == 'reverse'):
            my_list.reverse()
        elif ( cmd == 'sort'):
            my_list.sort()
        elif ( cmd == 'print'):
            print (my_list)           