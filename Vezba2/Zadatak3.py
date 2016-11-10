def zad3(n,m):
    sum=0
    if len(n) != len(m):
        print "Vektori moraju biti istih dimenzija"
        return False
    else:
        for i in (range(len(n))):
            sum+=n[i] * m[i]
    return sum

if __name__ == "__main__":
    print zad3([2,2,2,2],[3,3,3,3])