#function to return factors of num, includes 1 and num
def listfactors(num):
    count = 0
    factors = []
    
    for p in range(1,int(num**0.5)+1):
        if num%p == 0:
            factors.append(p)
            factors.append(num/p)
            #print p,num/p
            count = count + 2 #each small factor has a bigger half of the pair
            
    factors = set(factors)
    sortedfactors = sorted(factors)
    del sortedfactors[len(factors)-1]
    return sortedfactors



perfect = []
for k in range(2,500000):
    propdiv = listfactors(k)
    #print k, sum(propdiv), propdiv
    if k == sum(propdiv):
        perfect.append(k)
print "perfect:",perfect
