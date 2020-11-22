import random
import itertools
import re

kod1 = random.randint(33,58)
kod2 = random.randint(33,58)
dlugosc = 3#random.randint(1,2)

print(kod1,kod2,dlugosc)

x = list(map(lambda a: chr(a),range(min(kod1,kod2),max(kod1,kod2)+1)))


comb = list(map(lambda b: ''.join(b), list(itertools.combinations_with_replacement(x,dlugosc))))



q = list(filter(lambda c: re.match('^[0-9]*', c).group(),comb))
print(q)

tab = []
w = list(filter(lambda d: tab.append(d) and len(re.match('^[0-9]*', d).group()) <= dlugosc-1, q))
print(tab)
