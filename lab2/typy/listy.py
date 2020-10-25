#!/bin/bash env python3

from typy import lista


def zapisz(znaki):
    for i in "0123456789":
        if znaki.count(i) != 0:
            lista.append(i)
            lista.append(znaki.count(i))


def wypisz():
    wyjscie = ""
    for i in range(len(lista)):
        if i % 2 == 0:
            wyjscie = wyjscie + str(lista[i]) + ":"
        else:
            wyjscie = wyjscie + str(lista[i])
            if i != len(lista) - 1:
                wyjscie = wyjscie + ", "
    print(wyjscie)
