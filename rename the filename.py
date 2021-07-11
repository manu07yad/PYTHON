import os

oldname= "copy.txt"
newname= "name.txt"
with open (oldname) as f:
     content= f.read()

with open (newname,"w") as f:
     f.write(content)

os.remove(oldname)

