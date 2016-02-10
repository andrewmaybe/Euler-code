#function to return count of factors for any number, includes 1 and num
def countfactors(num):
    count = 0
    for p in range(1,int(num**0.5)+1):
        if num%p == 0:
            #print p,num/p
            count = count + 2 #each small factor has a bigger half of the pair
            
    return count

x = 0
import time
start = time.time()
x = countfactors(760000000000)
end = time.time()
print end - start, x

