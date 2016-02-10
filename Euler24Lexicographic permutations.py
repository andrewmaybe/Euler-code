import itertools

L = range(10)
perms = []

for x in itertools.permutations(L):
    p = list(x)
    perms.append(p)
    
print len(perms), perms[999999]

