from math import pi,degrees
def zad3():
    pravac1 = raw_input("Unesite prvi pravac u formatu (stepen,minut,sekund):\t")
    pravac2 = raw_input("Unesite drugi pravac u formatu (stepen,minut,sekund):\t")

    st1,m1,se1 = pravac1.split(",")
    st2,m2,se2 = pravac2.split(",")
    PR1 = float(st1)+float(m1)/60.0+float(se1)/3600.0
    PR2 = float(st2)+float(m2)/60.0+float(se2)/3600.0
    ugao = PR2 - PR1
    ugaoRad = ugao * pi/180
    print "Razlika dva pravca daje ugao vrednosti %.4f stepeni"%(degrees(ugaoRad))




