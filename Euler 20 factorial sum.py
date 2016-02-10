#Find the sum of the digits in the number 100!

factorial = 1
num = 10
for n in range(100,1,-1):
    factorial = factorial * n
print factorial
stringfac = str(factorial)
factsum = 0
for c in stringfac:
    factsum = factsum + int(c)
print factsum
