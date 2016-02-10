datafile = open("p022_names.txt")
rawdata = datafile.read()
dataarray = []
dataarray2 = []
dataarray = rawdata.split(",")
for n in dataarray:
    n = n[1:-1]
    dataarray2.append(n)
dataarray2.sort()

count = 0
totalscore = 0
for p in dataarray2:
    value = 0
    count = count + 1
    for c in p:
        value = value + ord(c)-64
        namescore = value * count
    totalscore = totalscore + namescore    
    #print dataarray2[p],value, count, namescore, totalscore    
print totalscore

    

