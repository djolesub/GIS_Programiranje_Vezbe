def zad6():
    num1 = int(raw_input("Unesite prvi broj: "))
    num2 = int(raw_input("Unesite drugi broj: "))
    if num1 == num2:
        print "Unesene vrednosti moraju biti razlicite.\nMilomo Vas pokusajte ponovo"
    else:
        if num1 < num2:
            print "Minumun je %d a maksimum %d"%(num1,num2)
        else:
            print "Minumun je %d a maksimum %d"%(num2,num1)
if __name__ == "__main__":
    zad6()