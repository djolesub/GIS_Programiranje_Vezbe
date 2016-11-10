from math import sqrt
def zad2():
    print "Unesite koeficijente kvadratne jednacine: \n"
    a = float(raw_input("Unesite vrednost za a: \t"))
    b = float(raw_input("Unesite vrednost za b: \t"))
    c = float(raw_input("Unesite vrednost za c: \t"))

    vrstaResenja = [('Realni',0),('Dvostruki',1),('Kompleksni',2),('Linearna',3),('Pogresna',4)]

    x1,x2 = 0,0 #Realni deo korena
    y1,y2 = 0,0 #Imaginarni deo korena

    if a != 0:
        d = b**2 - 4*a*c
        if d>0:
            vrsta = vrstaResenja[0][0]
            x1 = (-b+sqrt(d))/(2*a)
            x2 = (-b-sqrt(d))/(2*a)
        elif d==0:
            vrsta = vrstaResenja[1][0]
            x1 = -b/(2*a)
        else:
            vrsta = vrstaResenja[2][0]
            x1 = -b/(2*a )
            y1 = sqrt(-d)/(2*a)
            x2 = x2
            y2 = -y1

    else:
        if b != 0:
            vrsta = vrstaResenja[3][0]
            x1 = -c/b
        else:
            vrsta = vrstaResenja[4][0]

    if vrsta == "Realni":
        print "Realni koreni su: %.2f i %.2f"%(x1,x2)
    elif vrsta == "Dvostruki":
        print "Dvostruki realni koreni su: %.2f"%(x1)
    elif vrsta == "Kompleksni":
        print "Kompleksni koreni su %.2f,%.2f i %.2f,%.2f"%(x1,y1,x2,y2)
    elif vrsta == "Linearna":
        print "Resenje linearne jednacine je %.2f"%(x1)
    elif vrsta == "Pogresna":
        print "Podaci nisu validni.Pokusajte ponovo"

if __name__ == "__main__":
    zad2()