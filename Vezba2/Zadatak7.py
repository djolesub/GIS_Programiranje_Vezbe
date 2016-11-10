def zad7(n):
    return reduce(lambda x,y:x+y,n)

if __name__=="__main__":
    print zad7([1,2,3,4,5,6,7,8,9])