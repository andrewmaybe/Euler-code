#Find the sum of all numbers,less than one million,
#which are palindromic in base 10 and base 2.

def palindrome(instring):
    
    if type(instring) != 'str':
        instring = str(instring)

    instring = instring.lstrip('0')

    if instring == instring[::-1]:
        return True
    else:
        return False

tot = 0
r=0
while r<1000001:
    rbin = "{0:#b}".format(r).lstrip('0b')
    if palindrome(r) and palindrome(rbin):
        tot=tot+r
        print r,rbin,tot
    r=r+1
    
