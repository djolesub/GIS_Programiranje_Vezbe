def zad13():
    num = raw_input("Unesite vrednosti za n i k u formatu (n,k):\t ")
    n,k = num.split(",")
    try:
        n = int(n)
        k = int(k)
    except ValueError:
        print "Unesene vrednosti moraju biti integer-i"

    if n<0:
        m = (int(n)/int(k))+1
        print "Broj %d se sadrzi u broju %d %d puta"%(k,n,abs(m))
    elif k<0:
        m = (int(n)/int(k))+1
        print "Broj %d se sadrzi u broju %d %d puta"%(k,n,abs(m))
    else:
        m = (int(n)/int(k))
        print "Broj %d se sadrzi u broju %d %d puta"%(k,n,abs(m))

if __name__ == "__main__":
    zad13()
