#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

num = 2000000
psum = 0 #sum of primes
count = 0 #count of primes
#primes = []
for num in range(2,num,1):  
   for i in range(2,int(num**0.5)+1): 
      if num%i == 0:      
         break 
   else:                  
      count=count+1
      psum = psum + num
      #primes.append(num)
print count, psum
#print primes




    
