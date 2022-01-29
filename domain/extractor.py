import unidecode
import os
import re

def getWords(line, ending):
    aux = ending.split()
    count = len(aux[0])
    words = line.split()
    paraula1 = words[0]
    if re.match('^.*([0-9])$',paraula1):
        paraula1 = paraula1[0:len(paraula1)-1]
    paraula2 = words[1][1:]
    paraula2 = paraula1[0:len(paraula1) - count] + paraula2
    return paraula1, paraula2


# Look for your absolute directory path
absolute_path = os.path.dirname(os.path.abspath(__file__))
# Or: file_path = os.path.join(absolute_path, 'folder', 'my_file.py')

data = open(absolute_path + '/data.txt','r')
sol = open(absolute_path + '/semi-net.txt','w')
for line in data:
    # if re.match('^.*( -).*$', line):
    #     paraula1, paraula2 = getWords(line)
    #     to_print = paraula1 + "\n" + paraula2
    # else:
    #     to_print = line

    # print(to_print, file=sol)

    if "at -ada" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1)-2]+paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print,file=sol)
    elif "it -ida" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 2] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "iu -iva" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 2] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif re.match('^.*(-a)$',line):
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        if re.match('^.*([0-9])$', paraula1):
            paraula1 = paraula1[0:len(paraula1)-1]
        if re.match('^.*(e|o)$',paraula1):
            paraula2 = paraula1[0:len(paraula1)-1] + paraula2
        else:
            paraula2 = paraula1 + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif re.match('^.*([0-9])$',line):
        to_print = line[0:len(line) - 2]
        print(to_print, file=sol)
    elif "ari -ària" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 3] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "ià -ana" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 1] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "ut -uda" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 2] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "ós -osa" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 2] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "ini -ínia" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 3] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "ori -òria" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 3] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "emi -èmia" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 3] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "ès -esa" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 2] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "ó -ona" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 1] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "ec -ega" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 2] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "centè -centena" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 5] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "cents -centes" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 5] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "è -ena" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 1] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "opi -òpia" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 3] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "í -ina" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 1] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "eri -èria" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 3] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "ís -isa" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 2] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "aci -àcia" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 3] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "igi -ígia" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 3] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "oli -òlia" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 3] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "ogen -ògena" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 4] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "idi -ídia" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 3] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "ici -ícia" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 3] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "ís -issa" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 2] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "oni -ònia" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 3] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "ogin -ògina" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 4] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "obi -òbia" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 3] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "à -ana" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 1] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "òs -ossa" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 2] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "omfi -òmfia" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 4] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "ït -ïda" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 2] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "au -ava" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 2] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "òs -osa" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 2] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "ès -essa" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 2] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "oc -oga" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 2] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "í -ïna" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 1] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "omi -òmia" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 3] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "às -assa" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 2] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "urni -úrnia" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 4] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "esi -èsia" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 3] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "eu -ea" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 2] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "igin -ígina" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 4] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "or -ora" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 2] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "ic -iga" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 2] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "api -àpia" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 3] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "ú -ua" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 1] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "ús -ussa" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 2] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "ili -ília" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 3] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "ani -ània" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 3] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "ús -usa" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 2] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "ergen -èrgena" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 5] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "igen -ígena" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 4] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "ic -ica" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 2] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "indi -índia" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 4] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "ibi -íbia" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 3] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "isci -íscia" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 4] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "íac -íaca" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 3] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "àleg -àloga" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 4] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "òleg -òloga" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 4] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "agen -àgena" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 4] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "eni -ènia" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 3] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)

    elif "idu -ídua" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 3] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "iri -íria" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 3] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "uc -uga" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 2] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "uri -úria" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 3] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "ac -aga" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 2] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "oci -òcia" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 3] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "brú -una" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 3] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "ingi -íngia" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 4] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "er -era" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 2] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    elif "un -una" in line:
        aux = line.split()
        paraula1 = aux[0]
        paraula2 = aux[1][1:]
        paraula2 = paraula1[0:len(paraula1) - 2] + paraula2
        to_print = paraula1 + "\n" + paraula2
        print(to_print, file=sol)
    else:
        to_print = line[0:len(line)-1]
        print(to_print, file=sol)

sol.close()
data.close()
