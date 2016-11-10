def zad9(n,m,flag = "p"):
    flagOp = ('p','-p')
    rezultat = []
    if not flag in flagOp:
        print "Wrong flag parameter. Flag can be '-p' or 'p'"
        return False
    else:
        if flag == "p":
            rezultat.extend(n)
            rezultat.extend(m)
        elif flag == "-p":
            rezultat.extend(m)
            rezultat.extend(n)
        return rezultat

if __name__ == "__main__":
    flag = raw_input("Unesite flag parametar za kreiranje novig niza: ")
    print zad9([1,2,3,4],[5,6,7,8],flag=flag)