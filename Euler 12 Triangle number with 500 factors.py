#What is the value of the first triangle number
#to have over five hundred divisors?

#function to return count of factors for any number, includes 1 and num
def countfactors(num):
    count = 0
    for p in range(1,int(num**0.5)+1):
        if num%p == 0:
            #print p,num/p
            count = count + 2 #each small factor has a bigger half of the pair
            
    return count

#loops through all numbers, logging factor-count until above max, then break
TN = 0
n = 0
max = 499
factorcount = 0
biggest = 0
biggestTN = 0
cont = True
while cont == True:
    n = n+1
    TN = TN + n
    factorcount = countfactors(TN)
    if factorcount > biggest:
        biggest = factorcount
        biggestTN = TN
    #print TN, factorcount
    if factorcount > max:
        break
print "TN:",biggestTN,"# of factors:",biggest
