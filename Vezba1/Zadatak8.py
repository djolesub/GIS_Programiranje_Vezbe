def zad8():
    a = True
    while(a):
        try:
            num = raw_input("Unesite broj koji se sastoji od 5 cifara:\t")
            num = int(num)
            if len(str(num)) == 5:
                a = False
        except ValueError:
            print "Unesena vrednost je pogresna. Pokusajte ponovo"

    max = int(str(num)[0])
    for i in range(len(str(num))):
        if str(num)[i] > max:
            max=int(str(num)[i])
    print "Najveca cifra u unesenom broju je: %d"%(max)
