def zad7():
    num1 = raw_input("Unesite prvi broj:\t")
    num2 = raw_input("Unesite drugi broj:\t")
    num3 = raw_input("Unesite treci broj:\t")
    num4 = raw_input("Unesite cetvrtibroj:\t")

    try:
        val1 = int(num1)
    except ValueError:
        print "You must Enter Integer value"
        num1 = raw_input("Unesite prvi broj ponovo:\t")
    try:
        val2 = int(num2)
    except ValueError:
        print "You must Enter Integer value"
        num2 = raw_input("Unesite drugi broj ponovo:\t")
    try:
        val3 = int(num3)
    except ValueError:
        print "You must Enter Integer value"
        num3 = raw_input("Unesite treci broj ponovo:\t")
    try:
        val4 = int(num4)
    except ValueError:
        print "You must Enter Integer value"
        val4 = int(raw_input("Unesite cetvrti broj ponovo:\t"))

    sumL = [val1,val2,val3,val4]
    sum=0
    for i in sumL:
        if i >0:
            sum+=i
    print "Suma pozitivnih vredosti je: %d"%(sum)