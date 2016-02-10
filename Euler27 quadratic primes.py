import random

def isprime(n):
    if n<2: return False
    if n==2: return True
    for i in range(2,int(n**0.5)+1):   # only odd numbers
        if n%i==0:
            return False    
    return True

    #p = n**2+n+41
    #p = n**2-79*n+1601


#http://www.codeproject.com/Articles/691200/Primality-test-algorithms-Prime-test-The-fastest-w
def FermatPrimalityTest(number):
    
    if (number > 1):    #if number != 1       
        for time in range(3):   #repeat the test few times
            randomNumber = random.randint(2, number)-1  #Draw a RANDOM number in range of number(Z_number)            
            if (pow(randomNumber, number-1, number) != 1):    #Test if a^(n-1) = 1 mod n
                return False        
        return True
    else:   #case number == 1
        return False

result = dict()
biggestnsofar = 0
biggest = dict()
for a in range(-1000, 1000):
    for b in range (a, 1000):
        count = 0
        n = 1
        while FermatPrimalityTest(n**2 + a*n + b):
            n=n+1
        if n > biggestnsofar:
            biggestnsofar = n
            biggest = {'a':a,'b':b,'n':n,'ab':a*b}
            print biggest


