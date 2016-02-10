#Find the difference between the sum of the squares of the first
#one hundred natural numbers and the square of the sum.

#square of sum
sum1 = 0
sqofsum = 0
for n in range(1,101):
    sum1 = sum1 + n
sqofsum = sum1**2
print sum1
print sqofsum

#sum of squares
sum2 = 0
sumofsq = 0
for n in range(1,101):
    sq = n**2
    sumofsq = sumofsq+sq
print sumofsq

#difference
print sqofsum-sumofsq
