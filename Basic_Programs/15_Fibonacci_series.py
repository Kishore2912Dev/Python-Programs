num=int(input("enter number:"))
a,b=0,1
sum=0
if num <=0:
  print("enter the greatesrt number.")
else:
  for i in range(0,num):
    print(sum, end=" ")
    a=b
    b=sum
    sum=a+b
    