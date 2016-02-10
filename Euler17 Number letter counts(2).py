digits = ['','one','two','three','four','five','six','seven','eight','nine']
tens = ['','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
teens = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']

totalcharcount = 0
string = ''
for n in range(1,1000):
    numarr = map(int,list(str(n)))
    length = len(numarr)
    if length==1:
        string = digits[numarr[length-1]]
    if length==2:
        if numarr[length-2]==1: #then use teens
            string = teens[numarr[length-1]]
        else:
            string = tens[numarr[length-2]]+digits[numarr[length-1]]
    if length==3:
        if numarr[length-2]==0 and numarr[length-1]==0: #just for the round hundreds
            string = digits[numarr[length-3]]+'hundred'
        elif numarr[length-2]==1: #for the teens
            string = digits[numarr[length-3]]+'hundred'+'and'+teens[numarr[length-1]]
        else: #for the rest
            string = digits[numarr[length-3]]+'hundred'+'and'+tens[numarr[length-2]]+digits[numarr[length-1]]
    charcount = len(string)
    totalcharcount = totalcharcount + charcount
    print n, charcount, totalcharcount, string
totalcharcount = totalcharcount + len('onethousand')
print 1000,len('onethousand'),totalcharcount,'onethousand'
print totalcharcount





            
