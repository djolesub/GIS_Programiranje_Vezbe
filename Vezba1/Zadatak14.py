def zad14():
    num = raw_input("Unesite proizvoljnu celobrojnu vrednost:\t")
    if len(num) <2:
        print "Morate uneti bar dve cifre"
    else:
        sumParni=0
        sumNeparni=0
        for i in range(len(str(num))):
            if i%2 ==0:
                sumParni+=int(num[i])
            else:
                sumNeparni+=int(num[i])
        print "Apsolutna vrednost ralizke parnih i neparnih elemenata je %d "%(abs(sumParni - sumNeparni)  )

zad14()