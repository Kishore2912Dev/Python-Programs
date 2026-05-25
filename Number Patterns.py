
'''

#1. pattern 1
n=5
p=1
for i in range(n):
  for j in range(i+1):
    print(p,end=' ')
  print()
  p+=1

  '''


'''
#2.Pattern 2
n=5
p=5
for i in range(n):
  for j in range(i+1):
    print(p,end=' ')
  p-=1
  print()

  '''
'''
#3.Pattern 3
n=5
p=0
for i in range(n):
  for j in range(i+1):
    print(p,end=' ')
  p+=2
  print()

#4.Pattern 4
n=5
for i in range(n):
  for j in range(i+1):
    if (i%2==0):
      print('1',end=' ')
    else:
      print('2',end=' ')
  print()


  '''

'''
#5.Pattern 5
n=5
p=1
for i in range(n-1):
  for j in range(i,n):
    print(' ',end=' ')
  for j in range(i):
    print(p,end=' ')
  for j in range(i+1):
    print(p,end=' ')
  print()
  p+=1
for i in range(n):
  for j in range(i+1):
    print(' ',end=' ')
  for j in range(i,n-1):
    print(p,end=' ')
  for j in range(i,n):
    print(p,end=' ')  
  print()
  p+=1

  '''



'''
#6.Pattern 6
n=5
p=1
for i in range(n-1):
  for j in range(i,n):
    print(' ',end=' ')
  for j in range(i):
    print(p, end=' ')
  for j in range(i+1):
    print(p,end=' ')
  print()
  p+=1
for i in range(n):
  for j in range(i+1):
    print(' ',end=' ')
  for j in range(i,n):
    print(p,end=' ')
  for j in range(i,n-1):
    print(p,end=' ')
  print()
  p-=1

'''


'''
#7.Pattern 7
n=5
for i in range(n):
  p=5
  for j in range(i+1):
    print(p,end=' ')
    p-=1
  print()

  '''


'''
#8.Pattern 8
n=5
k=5
for i in range(n):
  p=k
  for j in range(i):
    print(' ',end=' ')
  for j in range(i,n):
    print(p ,end=' ')
    p-=1
  k-=1
  print()

  '''




'''
#9.Pattern 9
n=5
for i in range(n):
  p=1
  for j in range(i,n):
    print(' ',end=' ')
  for j in range(i):
    print(p,end=' ')
    p+=1
  for j in range(i+1):
    print(p,end=' ')
    p-=1
  print()

'''


#10.Pattern 10 [Floyd triangle]
n=4
p=1
for i in range(n):
  for j in range(i+1):
    print(p,end=' ')
    p+=1
  print()
