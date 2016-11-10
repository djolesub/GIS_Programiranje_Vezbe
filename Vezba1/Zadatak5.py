def zad5():
    num1 = int(raw_input("Unesite prvi broj:\t"))
    num2 = int(raw_input("Unesite drugi broj:\t"))
    num3 = int(raw_input("Unesite treci broj:\t"))

    numMed = abs(num1+num2+num3)/3
    print "Apsolutna vrednost aritmeticke sredine je: %.3f"%(numMed)

zad5()