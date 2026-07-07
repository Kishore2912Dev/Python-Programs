li=[int(x) for x in input("enter the list:").split()]
first=li[0]
last=li[-1]
if (first==last):
  print("same.")
else:
  print("not same.")