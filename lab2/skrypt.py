#!/bin/bash env python3

import re


wyrazy = re.compile(r'\D+')
liczby = re.compile(r'[0-9]+')

def wypisz_wyraz(napis):
    wyraz = ','.join(wyrazy.findall(napis))
    if wyraz:
        print("Wyraz: ", wyraz)
    return wyraz

def wypisz_liczbe(napis):
    liczba = ','.join(liczby.findall(napis))
    if liczba:
        print("Liczba: ", liczba)
    return liczba


if __name__ == '__main__':
    while (True):
        napis = input()

        wypisz_wyraz(napis)
        wypisz_liczbe(napis)

        '''wyraz = ','.join(wyrazy.findall(napis))
        liczba = ','.join(liczby.findall(napis))

        if wyraz:
            print("Wyraz: ", wyraz)
        if liczba:
            print("Liczba: ", liczba)'''
