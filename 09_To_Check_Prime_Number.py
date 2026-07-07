num=int(input("enter the numbber:"))
if num==1:
  print("it is not prime.")
elif num>1:
  for i in range(2, num):
    if num % i == 0:
      print("it is not prime")
      break
    else:
      print("it is prime.")