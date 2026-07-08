x=[[1,2,3],
    [2,3,4],
    [4,5,6]] 
result=[[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range(len(x)):
  for j in range(len(x[0])):
    result[i][j] = x[j][i]
print(result)
