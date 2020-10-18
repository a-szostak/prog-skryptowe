#!/bin/bash env python3

import sys, getopt
from typy import listy, slowniki


opts, args = getopt.getopt(sys.argv[1:], "", ["moduł:"])


znaki = input()

if ''.join(args) == "lista":
    listy.zapisz(znaki)
    listy.wypisz()
elif ''.join(args) == "slownik":
    slowniki.zapisz(znaki)
    slowniki.wypisz()
