import os

class Processor:

    def __init__(self):
        # Look for your absolute directory path
        absolute_path = os.path.dirname(os.path.abspath(__file__))
        # Or: file_path = os.path.join(absolute_path, 'folder', 'my_file.py')
        self.data = open(absolute_path + '/data.txt', 'r')
        self.abecedari = "abcdefghijklmnopqrstuvwxyzç123456789"

    def generate_solution(self, letters):
        no_interessa = [c in letters for c in self.abecedari]
        lletres_no = ""
        for i in range(len(no_interessa)):
            if no_interessa[i] == 0:
                lletres_no += self.abecedari[i]
        solucio = []
        for line in self.data:
            aux = [c in line for c in lletres_no]
            if 1 not in aux:
                if 1 in [c in line for c in letters[0]]:
                    if len(line) > 3:
                        solucio.append(line)
        self.data.close()
        return solucio
