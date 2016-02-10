

p=0
palinbig = 0
test = -1
largea = 0
largeb = 0
n = 20
for a in range(n, n * 3 / 4,-1):
    for b in range (a, n * 3 / 4,-1):
        p = a*b
        ps = str(p)
        prs = ps[::-1]
        pr = int(prs)
        
        if (p==pr): #if palindrome
            if (p > palinbig):
                palinbig = p
                largea = a
                largeb = b
print "p:",p,"pr:",pr
print "largea:",largea,"largeb:",largeb
print "palinbig",palinbig
