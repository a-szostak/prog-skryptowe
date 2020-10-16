#!/bin/bash env python3

import re


wyrazy = re.compile(r'[a-zA-Z]+')
liczby = re.compile(r'[0-9]+')


while (True):
    napis = input()

    wyraz = ','.join(wyrazy.findall(napis))
    liczba = ','.join(liczby.findall(napis))

    if wyraz:
        print("Wyraz: ", wyraz)
    if liczba:
        print("Liczba: ", liczba)
