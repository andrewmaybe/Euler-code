#find the 10001st prime starting with 2



largest = 0
count = 0
maxcount = 10001
num = 2
primeslist = []
while count<maxcount: 
   for i in range(2,int(num**0.5)+1):   
      if num%i == 0:      
         break 
   else:                  
      count=count+1
      largest = num
      #primeslist.append(num) 
   num = num+1


print count
print largest
