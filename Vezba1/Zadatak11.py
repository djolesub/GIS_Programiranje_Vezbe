import sys
def zad11():
    A = [10,15]
    B = [1,20]
    C = [4,17]
    print "Trougao je zadata sledecim tackama:"
    print "Tacka A ",A
    print "Tacka B ",B
    print "Tacka C ",C
    point = raw_input("Unesite vrednost tacke u formatu (x,y)za koju zelite da proverite da li je u poligonu:\t")
    p = point.split(",")
    M = [float(p[0]),float(p[1])]

    P = abs(A[0]*(B[1]-C[1]) + B[0]*(C[1]-A[1]) + C[0]*(A[0]-B[0]))/2

    P1 = abs(A[0] * (B[1] - M[1]) + B[0] * (M[1] - A[1]) + M[0] * (A[0] - B[0])) / 2
    P2 = abs(M[0] * (B[1] - C[1]) + B[0] * (C[1] - M[1]) + C[0] * (M[0] - B[0])) / 2
    P3 = abs(A[0] * (M[1] - C[1]) + M[0] * (C[1] - A[1]) + C[0] * (A[0] - M[0])) / 2

    if P == (P1 + P2 + P3):
     print('Tacka M ' , M , " pripada trouglu")
    else:
        print('Tacka M', M, " ne pripada trouglu")
if __name__ == "__main__":
    zad11()


