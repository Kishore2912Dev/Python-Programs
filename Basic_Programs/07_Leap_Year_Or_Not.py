num=int(input("enter:"))
if (num % 400 == 0 ) and (num % 100 == 0):
  print("it is leap year")
elif (num % 4 == 0) and (num % 100 != 0):
  print("it is leap year")
else:
  print("it is not leap year")
  