def zad9():
    a = True
    while(a):
        caracter = raw_input("Unesite proizvoljan karakter ili nulu da prekinete:\t")
        #print "Caracter je: %d"%(int(caracter))
        if caracter == "0":
            a = False
        if len(caracter) > 1:
            print "Mozete uneti samo jedan karakter. Molimo Vas pokusajte ponovo."
        carASC = ord(caracter)
        if caracter.isalpha():
            if caracter.isupper():
                print "Uneseni karakter: %s,ASCII:%d"%(caracter,carASC)
                print "Malo slovo: %s,ASCII: %d "%(caracter.lower(),ord(caracter.lower()))
            elif caracter.islower():
                print "Uneseni karakter: %s,ASCII: %d "%(caracter,carASC)
                print "Veliko slovo: %s,ASCII: %d "%(caracter.upper(),ord(caracter.upper()))
        else:
            print "Uneseni karakter: %s,ASCII: %d"%(caracter,carASC)

if __name__ == "__main__":
    zad9()