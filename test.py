
a = [[1,2,3],[4,5,6],['a','b']]
b = [[1,2,4],[4,8,6],['c',3]]
c = []
for i in range(len(a)) :
    for j in range(len(a[i])):
        if a[i][j] != b[i][j]:
            print(i,j)
