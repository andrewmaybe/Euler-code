import itertools
iterable = (1,2,5,10,20,50,100)
result = itertools.combinations_with_replacement(iterable, 200)
count = 0
for r in result:
    if sum(r) == 200:
        count = count + 1
        #print r
print "totalcount:",count
