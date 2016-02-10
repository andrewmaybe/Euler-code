#http://www.codeproject.com/Articles/691200/Primality-test-algorithms-Prime-test-The-fastest-w
import random
def FPT(number): #FermatPrimalityTest
    
    if (number > 1):    #if number != 1       
        for time in range(5):   #repeat the test few times
            randomNumber = random.randint(2, number)-1  #Draw a RANDOM number in range of number(Z_number)            
            if (pow(randomNumber, number-1, number) != 1):    #Test if a^(n-1) = 1 mod n
                return False        
        return True
    else:   #case number == 1
        return False

#all primes are odd and end in 1,3,7,9
#truncatable must be made entirely of these numbers

import itertools

def trunc(p): #string arg. returns true if prime is truncatable
    g = 1
    tr = True
    while g<len(p) and tr == True:
        #print int(p[g:]),int(p[:-g])
        if  FPT(int(p[g:])) and FPT(int(p[:-g])):
            tr = True
        else:
            tr = False
        g = g + 1    
    return tr       
'''
#testing the repeatability of the FPT
count = 0
for a in range(10000):
    if trunc("79337"):
        count = count+1
print count
    
'''
iterset = "0123579"
tot = 0
count = 0
s = 2
while s < 8:    
    for i in itertools.product(iterset,repeat=s):
        a = ''.join(i) #string
        if FPT(int(a)):
            if(trunc(a))==True:
                count = count + 1
                tot = tot + int(a)
                print count, a, tot
    s = s + 1
    
