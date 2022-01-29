import os
import unidecode


class Processor:

    def __init__(self):
        # Look for your absolute directory path
        absolute_path = os.path.dirname(os.path.abspath(__file__))
        # Or: file_path = os.path.join(absolute_path, 'folder', 'my_file.py')
        self.data = open(absolute_path + '/net.txt', 'r')
        self.abecedari = "abcdefghijklmnopqrstuvwxyzç"

    def generate_solution(self, letters):
        no_interessa = [c in letters for c in self.abecedari]
        lletres_no = ""
        for i in range(len(no_interessa)):
            if no_interessa[i] == 0:
                lletres_no += self.abecedari[i]
        solucio = []
        tutis = []
        for line in self.data:
            normalized_line = unidecode.unidecode(line)
            aux = [c in normalized_line for c in lletres_no]
            if 1 not in aux:
                if 0 not in [c in normalized_line for c in letters]:
                    tutis.append(line)
                elif 1 in [c in normalized_line for c in letters[0]]:
                    if len(normalized_line) > 3:
                        if line not in solucio:
                            solucio.append(line)
        self.data.close()
        return solucio, tutis
