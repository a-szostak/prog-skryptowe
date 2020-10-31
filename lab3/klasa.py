#!/bin/bash env python3

class Klasa(object):

    tab = [1,2,3]

    def __init__(self, tab, _zmienna1, __zmienna2):
        self.tab = tab
        self._zmienna1 = _zmienna1
        self.__zmienna2 = __zmienna2
        print("Wywołano metodę '__init__()'")

    def __del__(self):
        print("Wywołano metodę '__del__()'")

    def __str__(self):
        return "Wywołano metodę '__str__()'"

    def metodaInstancyjna(self):
        print(Klasa.tab)
        print(self.tab)
        print("Wywołano metodę 'metodaInstancyjna()'")

    @classmethod
    def metodaKlasowa(cls):
        print("Wywołano metodę 'metodaKlasowa()'")

    @staticmethod
    def metodaStatyczna():
        print("Wywołano metodę 'metodaStatyczna()'")
