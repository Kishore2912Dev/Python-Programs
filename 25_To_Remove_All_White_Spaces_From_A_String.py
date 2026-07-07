import re
text="hiii          buddy      ... "
print("original:",text)
print("by removing spaces:", re.sub(r'\s+','',text))