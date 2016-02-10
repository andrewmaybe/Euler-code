#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
import time
start = time.time()
PF = 'none'

#number = 600851475143
#pass1
number = 600851475143
for i in range(2,int(number**0.5),1):
    if number%i == 0:
        PF = number/i
        break
print "number:",number,"PF",PF
#pass2
number = int(PF)
for i in range(2,int(number**0.5),1):
    if number%i == 0:
        PF = number/i
        break
print "number:",number,"PF:",PF
#pass3
number = int(PF)
for i in range(2,int(number**0.5),1):
    if number%i == 0:
        PF = number/i
        break
print "number:",number,"PF:",PF
#pass4
number = int(PF)
for i in range(2,int(number**0.5),1):
    if number%i == 0:
        PF = number/i
        break
print "number:",number,"PF:",PF
#hopefully got it by now
end = time.time()
elapsed = end-start
print elapsed,"s"

    


