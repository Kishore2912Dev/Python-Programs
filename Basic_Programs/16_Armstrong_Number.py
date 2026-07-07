num=int(input("enter the number:"))
temp=num
sum=0
power=len(str(num))
while temp>0:
  digit = temp % 10
  sum += digit**power
  temp //=10
if sum == num:
  print("armstrong number.")
else:
  print("not an armstrong number.")