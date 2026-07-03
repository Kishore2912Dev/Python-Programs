punctuations=" '  ! @ # $ % ^ & * () _ + = . "
my_str=str(input("enter the string:"))
new_str= " "
for z in my_str:
  if z not in punctuations:
    new_str+= z
print(new_str)