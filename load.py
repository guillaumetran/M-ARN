#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def usage():
  print("Usage : [name] [symbol] [txt]")
  print("Exemple : >rna AGCAGGGCAGAAGCCCACAUGGUU ....((((....))((....))))")
  sys.exit(0)

def check(symbol, sequence):
    if len(symbol) != len(sequence):
        print ("Symbol and sequence me be same size")
        sys.exit(0)


if __name__ == '__main__':
    if len(sys.argv) != 4 :
        usage()
    nameMolecul = sys.argv[1]
    SymbolMolecul = sys.argv[2]
    TxtMolecul = sys.argv[3]
    check(SymbolMolecul, TxtMolecul)
