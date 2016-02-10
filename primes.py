count = 0
import time
start = time.time()
for num in range(1,10000,2):  
   for i in range(2,int(num**0.5)): 
      if num%i == 0:      
         break 
   else:                  
      count=count+1
end = time.time()
elapsed = end-start
print count,"in",elapsed,"s"
