import sys
def zad2():
    """
    Aritmetika sa dva unesena broja
    """
    print "Unesite prvi broj:\t"
    num1 = int(sys.stdin.readline())
    print "Unesite drugi broj:\t"
    num2 = int(sys.stdin.readline())
    if isinstance(num1,int) and isinstance(num2,int) and num2 != 0:
        print "Uneseni brojevi su: %d i %d\n" %(num1,num2)
        zbir = num1+num2
        razlika=num1-num2
        proizvod = num1*num2
        ceo = num1/num2
        ostatak = num1%num2
        print "Zbir:%d"%(zbir)
        print "Razlika:%d"%(razlika)
        print "Proizvod:%d"%(proizvod)
        print "Ceo:%d"%(ceo)
        print "Ostatak:%d"%(ostatak)


