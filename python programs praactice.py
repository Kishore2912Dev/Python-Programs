'''1.add two numbers 
a=int(input("enter num1:"))
b=int(input("enter num2:"))
print(a+b)
'''


'''
#2.finding square root
num=64
sqr=num**(1/2)
print(sqr)
'''

'''
#3.calculate area of triangle
h=int(input("enter:"))
b=int(input("enter:"))
formula=(1/2)*b*h
print("area of triangle:",formula)
'''

'''
#4.swapping numbers
num1=10
num2=20
temp=num1
print("temp value:",temp)
num1=num2
print('val of num1:',num1)
num2=temp
print("value of num2:",num2)


'''
'''
#or

x=10
y=20
x,y = y,x
print("value of x :",x)
print("value of y:",y)

'''
'''
#5.Check if a number is positve, negative or zero
num=int(input("enter number:"))
if num>0:
  print("Positive")
elif num<0:
  print("negative")
else:
  print("zero")
  '''

'''
#6.check if a number is even or odd.
num=int(input("enter num:"))
if num % 2 == 0:
  print("even")
else:
  print("odd")

'''

'''
#7.check if a year is leap year or not.
num=int(input("enter:"))
if (num % 400 == 0 ) and (num % 100 == 0):
  print("it is leap year")
elif (num % 4 == 0) and (num % 100 != 0):
  print("it is leap year")
else:
  print("it is not leap year")

'''


'''
#8.finfing largest among 3 numbers.
num1=10
num2=20
num3=30
if (num1>num2) and (num1>num3):
  print("num1 is largest.")
elif (num2>num1) and (num2>num3):
  print("num2 is larger.")
elif (num3>num1) and (num3>num2):
  print("num3 is larger.")

  '''


'''
#9.program to check the prime nuber
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

'''

'''
#10.generate random number.
import random
num=random.randint(1,10)
print(num)

'''

'''
#11.to print all prime numbers in an interval.
low_limit=int(input("enter:"))
upper_limit=int(input("enter:"))
for num in range(low_limit, upper_limit+1):
  if num>1:
    for i in range(2,num):
      if num%2==0:
        break
    else:
      print(num)
'''

'''
#12. to convert celsius to fahrenheit.
celsius=int(input("enter:"))
fahrenheit = (celsius * (9/5)) +32
print("fahrenheit result is :",fahrenheit)

'''


'''
#13.finding factorial of number.
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
'''


'''
#14.Print multiplication table.
n=10
for i in range(1,10+1):
  print(n, "x", i ,"=", n*i)

#or
n=7
i=1
while i<=5:
  print(n, "x", i , "=", n*i)
  i+=1

'''

'''
#15.Fibonacci Series
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
'''


'''
#14.Armstrong number
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

'''


'''
#15.palindrome or not.
word="radar"
word1=word[::-1]
if (word==word1):
  print('palindrome')
else:
  print("not palindrome.")

'''

'''
#16.To print summ of all numbers in a list.
li=[1,2,3,4,5]
def sum(li):
  total=0
  for x in li:
    total+=x
  return total
print(sum(li))
'''


'''
#17.To add 2 numbers using map and lambda.
l1=[1,2,3]
l2=[2,3,4]
print(l1)
print(l2)
sum=map(lambda x,y:x+y,l1,l2)
print(list(sum))
'''


'''
#18.to remove puctualtions from the string.

punctuations=" '  ! @ # $ % ^ & * () _ + = . "
my_str=str(input("enter the string:"))
new_str= " "
for z in my_str:
  if z not in punctuations:
    new_str+= z
print(new_str)
'''


'''
#19. To reverse a number.
num=str(int(input("enter the number:")))
num = num[::-1]
print(num)
'''


