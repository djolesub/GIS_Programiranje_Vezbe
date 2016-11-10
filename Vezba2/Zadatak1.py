def zad1(n):
    if n==0:
        return 1
    else:
        return n * zad1(n-1)

if __name__=="__main__":
    print zad1(5)
