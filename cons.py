from typing import Text, TextIO


def read_fasta(fasta_file: TextIO) -> str:
    value = ''
    for line in fasta_file:
        if line.startswith('>'):
            if value:
                yield value
                value = ''
        else:
            value += line.strip()
    yield value


def build_matrix(*fasta_seqs: Text) -> dict:
    matrix = {n: [0] * len(fasta_seqs[0]) for n in 'ACGT'}
    for fasta in fasta_seqs:
        for i in range(len(fasta)):
            matrix[fasta[i]][i] += 1
    return matrix

# add comment


def read_consensus(cons_matrix: dict) -> str:
    consensus = ''
    keys = list(cons_matrix.keys())
    for v in zip(*cons_matrix.values()):
        consensus += keys[v.index(max(v))]

    return consensus


if __name__ == '__main__':
    with open('C:\\Users\\gvandestee\\Downloads\\rosalind_cons.txt') as infile, open(
            "C:\\Users\\gvandestee\\Downloads\\rosalind_cons.txt.output.txt", "w") as outfile:
        fastas = read_fasta(infile)
        matrix = build_matrix(*fastas)
        outfile.write((read_consensus(matrix)) + '\n')
        for key, value in matrix.items():
            outfile.write("{}: {}".format(key, ' '.join(map(str, value))) + '\n')
