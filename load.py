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


#ptr = 0

if __name__ == '__main__':
    if len(sys.argv) != 4 :
        usage()
    nameMolecul = sys.argv[1]
    SymbolMolecul = sys.argv[2]
    TxtMolecul = sys.argv[3]
    checkSize(SymbolMolecul, TxtMolecul)
    checkFormatTxt(TxtMolecul)
    tabBracket = getTabBracket(TxtMolecul)
