#n = n/2 (n is even) and n = 3n + 1 (n is odd)

def countitems(n):
    count = 0
    while n > 1:
        if n%2==0:
            n=n/2
            count = count + 1
        else:
            n=3*n+1
            count = count + 1
    return count + 1 


longest = 0
number = 0
length = 0
num = 10 #set start here
while num <1000000: #set limit here
    length = countitems(num)
    if length > longest:
        longest = length
        number = num
    num = num + 1
print "limit num:",num,"longestnumber:",number,"has chain length:",longest
