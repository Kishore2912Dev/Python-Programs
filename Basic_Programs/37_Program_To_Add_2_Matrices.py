x=[[1,2,3],
    [2,3,4],
    [4,5,6]] 
y=[[2,2,3],
    [3,3,4],
    [4,5,6]]
result=[[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range(len(x)):
 for j in range(len(y[0])):
  result[i][j]=x[i][j] * y[i][j]
print(result)

