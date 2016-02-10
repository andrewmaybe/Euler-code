
m = 2
n = 3
count = 4
digits = 0
while digits<1000:
    mnext = n
    n = n + m
    m = mnext
    count = count + 1
    digits = len(str(n))
    print "count:",count,"digits:",digits
