def zad6(n):
    sum = 0
    for i in n:
        if i % 2 == 0:
            sum+=i
    return sum

if __name__=="__main__":
    print zad6([1,2,3,4,5,6,7,8,9,10])