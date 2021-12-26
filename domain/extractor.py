
import os
import re


# Look for your absolute directory path
absolute_path = os.path.dirname(os.path.abspath(__file__))
# Or: file_path = os.path.join(absolute_path, 'folder', 'my_file.py')
file_path = absolute_path + '/diec.txt'
f = open(file_path,'r')
data = open(absolute_path + '/data.txt','w')
for line in f.readlines():
    s = re.search("ent=(.+?)\^cat.*", line)
    if s is not None:
        print(s.group(1),file=data)
f.close()
data.close()
data = open(absolute_path + '/data.txt','r')
sol = open(absolute_path + '/sol.txt','w')
set = "iguaent"
not_set = 'bcdfhjklmopqrsvwxyzç123456789'
for line in data:
    aux = [c in line for c in set]
    aux2 = [c in line for c in not_set]
    if 1 not in aux2:
        if 1 in [c in line for c in "i"]:
            if len(line) > 2:
                print(line, file=sol)
sol.close()
data.close()
