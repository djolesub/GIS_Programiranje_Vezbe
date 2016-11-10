import sys
def zad4():
    num1 = raw_input("Unesite prvi broj:\t\n")
    num2 = raw_input("Unesite drugi broj:\t")
    if isinstance(int(num1),int) and isinstance(int(num2),int):
        len1 = len(num1)
        len2 = len(num2)
        if (len1 == 4 and len2 == 4):
            sum=0
            for i in num2:
                sum+=int(i)
            print "Suma cifara drugog broja:%d"%(sum)
            sumParni=0;
            sumNeparni=0;
            for i in (range(len(num1))):
                if i%2 == 0:
                    sumParni+=int(num1[i])
                else:
                    sumNeparni+=int(num1[i])
            razlika = sumParni - sumNeparni
            print "Razlika cifara na parnim i neparnim mestima je: %.3f"%(razlika)
        else:
            print "Uneseni brojevi moraju imati po cetiri cifre."

    else:
        print "Za svaki broj morate uneti po cetiri cifre. Samo vrednosti od 0-9 su dozvoljene"

