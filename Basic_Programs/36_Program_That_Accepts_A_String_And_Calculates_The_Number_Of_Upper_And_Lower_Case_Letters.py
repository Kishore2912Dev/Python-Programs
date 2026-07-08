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


# #using function.
# text ="hi buddy I Am Surya"
# def str_text(txt):
#     u_c=0
#     l_c=0
#     for i in text:
#       if i.isupper():
#         u_c+=1
#       elif i.islower():
#         l_c+=1
#       else:
#         pass
#     print(u_c,l_c)
# str_text(text)