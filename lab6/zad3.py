import sys,re

#long version:
inside_files = list(map(lambda x: re.sub('\n', ' ', open(x,"rt").read()).split(' '), sys.argv[1:]))

tab = []
def add(tab1):
    global tab
    tab = tab + tab1
    return tab

chained = list(map(lambda d: add(d) , inside_files))

even = list(filter(lambda a: a!='' and int(a)%2==0, chained[-1]))



#shorter one:
tab = []
even = list(filter(lambda a: a!='' and int(a)%2==0, list(map(lambda d: add(d) , list(map(lambda x: re.sub('\n', ' ', open(x,"rt").read()).split(' '), sys.argv[1:]))))[-1]))


print(len(even))
