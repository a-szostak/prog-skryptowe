#!/bin/bash env python3

from typy import slownik


def zapisz(znaki):
    for i in "0123456789":
        if znaki.count(i) != 0:
            slownik.update({i: znaki.count(i)})


def wypisz():
    wyjscie = ""
    for i in slownik:
        wyjscie = wyjscie + i + ":" + str(slownik[i])
        if i != list(slownik.keys())[-1]:
            wyjscie = wyjscie + ", "
    print(wyjscie)
