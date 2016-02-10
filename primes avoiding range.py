count = 0
import time
start = time.time()

maxnum = 200
num = 2
primeslist = []
while num<maxnum: 
   for i in range(2,int(num**0.5)+1):   
      if num%i == 0:      
         break 
   else:                  
      count=count+1
      primeslist.append(num)
   
   num = num+1

end = time.time()
elapsed = end-start
print count,"in",elapsed,"s"
print primeslist
