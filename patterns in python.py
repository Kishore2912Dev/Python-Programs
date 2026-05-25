'''
#1.pattern 1
n=5
for i in range(n):
  for j in range(n):
    print("*", end=' ')
  print()

'''
'''
#2.Pattern 2
n=5
for i in range(n):
  for j in range(i+1):
    print('*',end=' ')
  print()
'''


'''
#3.Pattern 3
n=5
for i in range(n):
  for j in range(i,n):
    print('*',end=' ')
  print()

'''


'''
#4.Pattern 4 [Right Triangle]
n=5
for i in range(n):
  for j in range(i,n):
    print(' ',end=' ')
  for j in range(i+1):
    print('*',end=' ')
  print()

  ''' 


'''
#Pattern 5 [Left triangle]
n=5
for i in range(n):
  for j in range(i+1):
    print(' ', end=' ')
  for j in range(i,n):
    print('*', end=' ')
  print()

'''

'''
#Pattern 6 [Hill Pattern]
n=5
for i in range(n):
  for j in range(i,n):
    print(' ',end=' ')
  for j in range(i):
    print('*',end=' ')
  for j in range(i+1):
    print('*',end=' ')
  print()
  
'''


'''
#7.Pattern 7 [Reverse Hill Pattern]
n=5
for i in range(n):
  for j in range(i+1):
    print(' ',end=' ')
  for j in range(i,n-1):
    print('*', end=' ')
  for j in range(i,n):
    print('*',end=' ')
  print()
  '''


#8.Pattern 8 [Diamond ]
n=5
for i in range(n-1):
  for j in range(i,n):
    print(' ',end=' ')
  for j in range(i+1):
    print('*',end=' ')
  for j in range(i):
    print('*',end=' ')
  print()
for i in range(n):
  for j in range(i+1):
    print(' ',end=' ')
  
  for j in range(i,n-1):
    print('*',end=' ')
  for j in range(i,n):
    print('*',end=' ')
  print()