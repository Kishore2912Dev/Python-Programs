low_limit=int(input("enter:"))
upper_limit=int(input("enter:"))
for num in range(low_limit, upper_limit+1):
  if num>1:
    for i in range(2,num):
      if num%2==0:
        break
    else:
      print(num)