num=int(input("enter number:"))
fact=1
if num<0:
  print("doesn't exist.")
elif num==0:
  print("fact is 1")
elif num>0:
  for i in range(1, num+1):
    fact=fact*i
print("fact is :",fact)