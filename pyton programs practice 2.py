'''
#20.To access keys and values in dict using items() function.
info = {"name":"Kishore", 'age':21}
for i,j in info.items():
  print(i,j)

'''

'''
#21. To find or detcet the no of local variables declrded in a function.
def pyt():
  name="raju"
  age="20"
  print(pyt.__code__.co_nlocals)

'''


'''
#22.To access a hyphen seperted sequence of words as input and output should be printed in sorted words.
items=[n for n in input ("enter the string:").split('-')]
items.sort()
print("-".join(items))

'''

'''
#23.To remove all white spaces from a string.
import re
text="hiii          buddy      ... "
print("original:",text)
print("by removing spaces:", re.sub(r'\s+','',text))
'''



'''
#24.to access index of a list using for loop and start the indexing with non zero value.
li=[10,23,34,53]
for index,value in enumerate(li, start=100):
  print(index,value)

  '''


'''
#25. to get current time.
import datetime 
print(datetime.datetime.now().time())
'''

'''
#26.to split a string using multile delimeters.
a="hi,buddy,i,am,surya"
b="hii buddy this is surya"
print(a.split())
print(b.split())

'''

'''
#27.extend a list without using builtin function (extend, append)
l1=[1,2,3,4]
l2=[7,8,9,0]
l1[:0]=l2
print(l1)

'''


'''
#28.to check of the first and last numbers of a list is the same or not.
li=[int(x) for x in input("enter the list:").split()]
first=li[0]
last=li[-1]
if (first==last):
  print("same.")
else:
  print("not same.")

  '''

'''
#29.To calculate the length of the string without using length function.
name="surya"
temp=0
for char in name:
  temp+=1
print(temp)

'''

'''
#30.To check if a key is already present in a dict or not.
my_dict= {1:"hi",2:"ram"}
if 2 in my_dict:
  print("present")
else:
  print("not present")


  '''

'''

#31.to get a substring of a string.
st="hi buddy i am learning python"
print(st[3:22])

'''




'''
#32.To get the last elemetn of the list.
li=[int(x) for x in input("enter the list:").split()]
print(li[-1])
'''


'''
#33.to triple all the numbers of a gvien list of integers using map.
num=[10,20,30]
result=map(lambda x:x*3,num)
print(list(result))

'''



'''
#34.Program that accepts a string and calculate the number of upper and lower case letters.
text ="hi buddy I Am Surya"
u_c,l_c=0,0
for i in text:
  if i.isupper():
    u_c+=1
  elif i.islower():
    l_c+=1
  else:
    pass
print(u_c,l_c)

'''


'''
#using function.
text ="hi buddy I Am Surya"
def str_text(txt):
    u_c=0
    l_c=0
    for i in text:
      if i.isupper():
        u_c+=1
      elif i.islower():
        l_c+=1
      else:
        pass
    print(u_c,l_c)
str_text(text)


 '''



'''
 #35.program to add 2 matrices.
x=[[1,2,3],
    [2,3,4],
    [4,5,6]] 
y=[[2,2,3],
    [3,3,4],
    [4,5,6]]
result=[[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range(len(x)):
 for j in range(len(y[0])):
  result[i][j]=x[i][j] * y[i][j]
print(result)


'''


'''
#36.To transpose a matrix using nested loop.
x=[[1,2,3],
    [2,3,4],
    [4,5,6]] 
result=[[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range(len(x)):
  for j in range(len(x[0])):
    result[i][j] = x[j][i]
print(result)

'''


'''
#37.to find the sum of natural numbers.
num = 5
if num < 0:
  print("invalid input")
else:
  sum = 0
  for i in range(1,num+1):
    sum += i
  print(sum)

  '''



'''
#38.to find a number divisible by another number.
for i in range(0,100):
  if i%10==0:
    print(i)
'''


'''
#39.to convert the decimal to binary,octal and hexadecimal.
decimal=int(input("enter a num:"))
print("conversions:")
print(bin(decimal),"in binary")
print(hex(decimal),"in hexadecimal")
print(oct(decimal),"in octal")

'''


'''
#40.to find ASCII value of character.
char="z"
print("the value of ascii is:",char,ord(char))

'''



'''
#41.to find hcf or gcd.
def findhcf(x,y):
  if x<y:
    smaller=x
  else:
    smaller=y
  for i in range(1,smaller+1):
    if (x%i==0) and (y%i==0):
      hcf = i
  return hcf
print("hcf of x and y is:",findhcf(12,18))

'''