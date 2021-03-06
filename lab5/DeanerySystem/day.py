
#!/bin/bash env python3

import math
from enum import Enum

class Day(Enum):
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6
    SUN = 7


    def difference(self, day):
        wynik = day.value - self.value

        if wynik > 3:
            wynik = wynik - 7
        elif wynik < -3:
            wynik = wynik + 7

        return wynik


def nthDayFrom(n, day):
    wynik = (day.value + n) % 7

    if wynik == 0:
        wynik = 7

    return Day(wynik)
