#Work out the first ten digits of the sum of the following
#one-hundred 50-digit numbers.

f = open('Euler13.txt','r')
content = f.readlines()
total = 0
for L in content:
    total = int(L) + total
print total

