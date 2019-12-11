class BinOctHexDec:
    def __init__(self,dec,maxwidth):
        self._dec = dec
        self._width = maxwidth
        self._oct = str(oct(dec))
        self._oct = self._oct[2:len(self._oct)]
        self._hex = str(hex(dec))
        self._hex = self._hex[2:len(self._hex)]
        self._bin = str(bin(dec))
        self._bin = self._bin[2:len(self._bin)]
    def __repr__(self):
        if(self._hex.isalnum()):
            self._hex = self._hex.upper()
        return "{0:>{width}} {1:>{width}} {2:>{width}} {3:>{width}}".format(self._dec,self._oct, self._hex, self._bin, width=self._width)    
        #return "{0} {1} {2} {3}".format(self._dec,self._oct,self._hex,self._bin)
    def __str__(self):
        if(self._hex.isalnum()):
            self._hex = self._hex.upper()  
        return "{0:>{width}} {1:>{width}} {2:>{width}} {3:>{width}}".format(self._dec,self._oct, self._hex, self._bin,width=self._width)    
        #return "{0} {1} {2} {3}".format(self._dec,self._oct,self._hex,self._bin)

def print_formatted(n):
    lst =[]
    maxwidth = len("{0:b}".format(n))
    for x in range(1,n+1):
        lst.append(BinOctHexDec(x,maxwidth))
    for x in lst:
        print(x)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)