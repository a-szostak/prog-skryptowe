import random
import itertools
import re

kod1 = random.randint(0,128)
kod2 = random.randint(0,128)
dlugosc = random.randint(1,5)


x = list(map(lambda a: chr(a),range(min(kod1,kod2),max(kod1,kod2)+1)))

comb = list(map(lambda b: ''.join(b), list(itertools.combinations_with_replacement(x,dlugosc))))

numbers = list(filter(lambda c: re.match('^[0-9]*', c).group(),comb))

tab = []
list(filter(lambda d: len(re.match('[0-9]*', d).group()) <= (dlugosc-1) and tab.append(d), numbers))

print(tab)

