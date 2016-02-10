#1p, 2p, 5p, 10p, 20p, 50p, 1 (100p) and 2 (200p)
count = 0
total = 0
for p1 in range(200,0,-1):
    tp1=p1*1
    print p1
    for p2 in range(100,0,-1):
        tp2=p2*2
        for p5 in range(40,0,-1):
            tp5=p5*5
            for p10 in range(20,0,-1):
                tp10=p10*10
                for p20 in range(10,0,-1):
                    tp20=p20*20
                    for p50 in range(4,0,-1):
                        tp50=p50*50
                        for p100 in range(2,0,-1):
                            tp100=p100*100
                            for p200 in range(1,0,-1):
                                tp200=p200*200
                                total = tp1+tp2+tp5+tp10+tp20+tp50+tp100+tp200
                                if total == 200:
                                    count = count + 1
                                    #print "yay", count
print count

