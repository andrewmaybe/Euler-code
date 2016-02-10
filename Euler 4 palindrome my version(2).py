#A palindromic number reads the same both ways. The largest palindrome
#made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

p=0
palinbig = 0
test = -1
largea = 0
largeb = 0
for a in range(999,1,-1):
    for b in range (999,1,-1):
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
