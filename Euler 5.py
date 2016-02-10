#2520 is the smallest number that can be divided by each of the numbers
#from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all
#of the numbers from 1 to 20?


testfrom = 11
testto = 20
answer = 0
testnum = testto #it will not be less than this
keepgoing = True
while keepgoing == True:
    for n in range(testfrom,testto+1): #NB does not include upper limit
        if testnum%n != 0:
            testnum = testnum + testto #next number
            break #if not a factor
        
    else: #it has found it
        answer = testnum #snag the answer
        keepgoing = False # break out of while loop    
        
print "answer:",answer

    
