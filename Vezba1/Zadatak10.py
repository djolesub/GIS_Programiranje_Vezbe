
def zad10():
    seq = raw_input("Unesite pet karaktera:\t")
    if len(seq)> 5 or len(seq) < 5:
        print "Morate uneti tacno pet karaktera"
    else:
        num=0
        for i in seq:
            if i.isdigit():
                num+=1
        print "U unesenom nizu ima %d cifara"%(num)
