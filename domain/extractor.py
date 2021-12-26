
import os
import re


# Look for your absolute directory path
absolute_path = os.path.dirname(os.path.abspath(__file__))
# Or: file_path = os.path.join(absolute_path, 'folder', 'my_file.py')

data = open(absolute_path + '/data.txt','r')
sol = open(absolute_path + '/net.txt','w')
for line in data:
    if "at -ada" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:4]
        paraula2 = paraula1[0:len(paraula1)-2]+paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print,file=sol)
    elif "it -ida" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:4]
        paraula2 = paraula1[0:len(paraula1) - 2] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "tiu -iva" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:4]
        paraula2 = paraula1[0:len(paraula1) - 2] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "siu -iva" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:4]
        paraula2 = paraula1[0:len(paraula1) - 2] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif line.endswith("1\n") or line.endswith("2\n"):
        to_print = line[0:len(line) - 2]
        print(to_print, file=sol)
    else:
        to_print = line[0:len(line)-1]
        print(to_print,file=sol)

sol.close()
data.close()
