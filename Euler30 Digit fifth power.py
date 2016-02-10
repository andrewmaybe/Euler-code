#Find the sum of all the numbers that can be written
#as the sum of fifth powers of their digits.

sumdig5 = 0
for n in range(2,1000000): #tried for bigger numbers but no extras
    digits = list(str(n))
    digits5 = sum([int(num)**5 for num in digits])
    if n == digits5:
        print "n:",n, "digits5:",digits5
        sumdig5 = sumdig5 + digits5
print "sumdigits5:",sumdig5       

