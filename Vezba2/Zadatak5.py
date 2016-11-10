def zad5(n,m):
    w,h = len(n),len(m[0])
    result = [[0 for x in range(w)] for y in range(h)]
    for i in range(len(n)):
        for j in range(len(m[0])):
            for k in range(len(m)):
                result[i][j] = n[i][k] * m[k][j]
    return result

if __name__=="__main__":
    a = [[1,2,3],[4,5,6],[7,8,9]]
    b = [[1,2,3],[4,5,6],[7,8,9]]
    print zad5(a,b)