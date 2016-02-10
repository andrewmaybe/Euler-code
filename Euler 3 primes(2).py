#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def isprime(num):
    for i in range(2,int(num**0.5)): 
        if num%i == 0:     
            return False
            break
        else:
            return True
        
largest = 0
upperlimit = 1000
isprimefactor = False
for number in range(3,upperlimit,1):
   if upperlimit%number == 0:
       isprimefactor = isprime(number)
       if isprimefactor == True: largest = number
           
print largest


    


