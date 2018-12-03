"""
http://rosalind.info/problems/lcsm/
"""
from datetime import datetime

from cons import read_fasta


def create_hash_table(fasta_string):
    length = len(fasta_string)
    return {fasta_string[i:j + 1] for i in range(length) for j in range(i, length)}


if __name__ == '__main__':
    start = datetime.now()
    with open('C:\\Users\\gvandestee\\Downloads\\rosalind_lcsm.txt') as infile, open(
            'C:\\Users\\gvandestee\\Downloads\\rosalind_lcsm.txt.output.txt'.format(__file__), "w") as outfile:

        fastas = list(read_fasta(infile))

        motif = ''
        hash_table = create_hash_table(fastas[0])
        for key in hash_table:
            if all({key in fasta for fasta in fastas}):
                if len(key) > len(motif):
                    motif = key

        outfile.write(motif + '\n')
    end = datetime.now()

    print(end - start)
