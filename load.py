#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def usage():
  print("Usage : [name] [symbol] [txt]")
  print("Exemple : >rna AGCAGGGCAGAAGCCCACAUGGUU ....((((....))((....))))")
  sys.exit(0)

def checkSize(symbol, sequence):
    if len(symbol) != len(sequence):
        print ("[-] Symbol and sequence me be same size")
        sys.exit(0)
    print ("[+] OK arguments size")

def checkFormatTxt(txt):
    bOpen = txt.count('(')
    bClose = txt.count(')')
    if bOpen != bClose:
        print ("[-] Bad number of brackets")
        sys.exit(0)
    print ("[+] OK brackets")


"""def getTabBracket(txt):
    tabBracks  = []
    flag = 1
    for i in range(0, len(txt)):
        if txt[i] == ")":
            #print ("%d flag %d" % (i , flag))
            flag += 1
            value = OpenB(txt[0:i], flag)
            print ("%d match avec %d" % (value, i))"""




def rewritestr(txt):
    tabBracks  = []
    while txt.find(')') != -1:
        for i in range(0, len(txt)):
            if txt[i] == ')':
                nb = txt[0:i].rfind('(')
                print ("La parenthese ouvrante N°%d match avec la parenthese ouvrante = N°%d"% (i, nb))
                s = list(txt)
                s[i] = 'x'
                s[nb] = 'x'
                txt = "".join(s)

                emptystr = "." * len(txt)
                n = list(emptystr)
                n[i] = ')'
                n[nb] = '('
                emptystr = "".join(n)
                tabBracks.append([nb,i])
                break
        print(emptystr)

    return (tabBracks)
        #print (txt)
            #print ("%c match avec = %c"% (txt[i], txt[nb]))


def getTabBracket(txt):
    tabOpen = []
    tabClose = []
    tabGlobal = []

    for i in range(0, len(txt)):
        if txt[i] == '(':
            tabOpen.append(i)
        if txt[i] == ')':
            tabClose.append(i)
    for k in range(0, len(tabOpen)):
        #print ("%d avec %d" % (k, len(tabOpen) -k - 1 ))
        tabGlobal.append([tabOpen[k],tabClose[len(tabOpen) -k - 1]])
    #print (tabOpen)
    #print (tabClose)
    print (tabGlobal)
    return (tabGlobal)


def fusion(tabBracket):
    bFusion = []
    for i in range(1, len(tabBracket)):
        #if (tabBracket[i][0]  + 1 == tabBracket[i - 1][0]  and tabBracket[i][0] == tabBracket[i - 1][0])
        if (tabBracket[i][0] == tabBracket[i - 1][0] + 1 and tabBracket[i][1] + 1 ==tabBracket[i - 1][1]):
            print ("On fusionne [%d,%d] avec [%d,%d]" %(tabBracket[i][0],  tabBracket[i][1] , tabBracket[i -1 ][0], tabBracket[i -1 ][1]))
        #    tabBracket[i - 1] = [0, 0]
    print (tabBracket)
#ptr = 0

if __name__ == '__main__':
    if len(sys.argv) != 4 :
        usage()
    nameMolecul = sys.argv[1]
    SymbolMolecul = sys.argv[2]
    TxtMolecul = sys.argv[3]
    checkSize(SymbolMolecul, TxtMolecul)
    checkFormatTxt(TxtMolecul)
    tabBracket = rewritestr(TxtMolecul)
    print (tabBracket)
    #tabBracket = getTabBracket(TxtMolecul)
    #fusion(tabBracket)
