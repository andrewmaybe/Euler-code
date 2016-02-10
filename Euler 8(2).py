
def getproduct(string13):
    product = 1
    for n in (string13):
        product = product * int(n)
    return product        

length = 4 #change to 13 after testing        
bigstring = "2817298474837389405485057973636"
value = 0
ss = ""
for c in (bigstring):
    
    ss = ss+c
    print  "ss",ss
    if len(ss) == length:
        value = getproduct(ss) #find product
        ss = ss[1:]# take the first character off
    print "value",value
